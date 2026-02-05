import csv
import sqlite3
import os
import re
from datetime import datetime

# Configuration
CSV_PATH = "../../1/Pen Test Database 1434c8e52376809da4d5d2b49e01cce9.csv"
MARKDOWN_DIR = "../../1/Pen Test Database"
DB_PATH = "pen_test.db"

def init_db(cursor):
    """Initialize the database schema."""
    cursor.execute("DROP TABLE IF EXISTS snippets")
    cursor.execute("DROP TABLE IF EXISTS technique_categories")
    cursor.execute("DROP TABLE IF EXISTS technique_platforms")
    cursor.execute("DROP TABLE IF EXISTS technique_technologies")
    cursor.execute("DROP TABLE IF EXISTS techniques_fts")
    cursor.execute("DROP TABLE IF EXISTS search_terms")
    cursor.execute("DROP TABLE IF EXISTS categories")
    cursor.execute("DROP TABLE IF EXISTS platforms")
    cursor.execute("DROP TABLE IF EXISTS technologies")
    cursor.execute("DROP TABLE IF EXISTS techniques")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS techniques (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    cursor.execute("CREATE TABLE IF NOT EXISTS categories (id INTEGER PRIMARY KEY, name TEXT UNIQUE)")
    cursor.execute("CREATE TABLE IF NOT EXISTS platforms (id INTEGER PRIMARY KEY, name TEXT UNIQUE)")
    cursor.execute("CREATE TABLE IF NOT EXISTS technologies (id INTEGER PRIMARY KEY, name TEXT UNIQUE)")
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS snippets (
        id INTEGER PRIMARY KEY,
        technique_id INTEGER,
        language TEXT,
        content TEXT,
        FOREIGN KEY(technique_id) REFERENCES techniques(id)
    )
    """)
    
    # Junction Tables
    cursor.execute("CREATE TABLE IF NOT EXISTS technique_categories (technique_id INTEGER, category_id INTEGER)")
    cursor.execute("CREATE TABLE IF NOT EXISTS technique_platforms (technique_id INTEGER, platform_id INTEGER)")
    cursor.execute("CREATE TABLE IF NOT EXISTS technique_technologies (technique_id INTEGER, technology_id INTEGER)")
    
    # Full Text Search
    cursor.execute("CREATE VIRTUAL TABLE IF NOT EXISTS techniques_fts USING fts5(title, description, content, technique_id UNINDEXED)")
    
    # Search Terms (Synonyms)
    cursor.execute("CREATE TABLE IF NOT EXISTS search_terms (term TEXT UNIQUE, expanded_query TEXT)")
    
    # Pre-populate search terms
    terms = [
        ("rce", "Execution OR 'Command Injection'"),
        ("bypass", "Defense Evasion OR 'Bypass'"),
        ("privesc", "'Privilege Escalation'"),
        ("lfi", "'Local File Inclusion' OR LFI"),
        ("xss", "'Cross Site Scripting' OR XSS")
    ]
    cursor.executemany("INSERT OR IGNORE INTO search_terms VALUES (?, ?)", terms)

def get_or_create(cursor, table, name):
    """Helper to get ID of a tag, creating it if needed."""
    if not name or not name.strip():
        return None
    name = name.strip()
    cursor.execute(f"SELECT id FROM {table} WHERE name = ?", (name,))
    res = cursor.fetchone()
    if res:
        return res[0]
    cursor.execute(f"INSERT INTO {table} (name) VALUES (?)", (name,))
    return cursor.lastrowid

def parse_markdown(file_path):
    """Extract code snippets from markdown."""
    snippets = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Regex for code blocks: ```lang ... ``` or just ``` ... ```
            # We use non-greedy matching for content
            matches = re.findall(r'```(.*?)\n(.*?)```', content, re.DOTALL)
            for lang, code in matches:
                snippets.append({'language': lang.strip() or 'text', 'content': code.strip()})

            # Fallback: specific handling for "LFI Bypass List" which uses a pipe table
            if not snippets and '|' in content:
                 # Extract table rows as a "snippet"
                 table_rows = re.findall(r'\|.*\|', content)
                 if table_rows:
                     snippets.append({'language': 'text', 'content': '\n'.join(table_rows)})
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return snippets

def clean_csv_field(field):
    """Extract clean names from CSV fields like 'Linux, Windows' or 'Reconnaissance (url)'."""
    if not field:
        return []
    # Remove Notion URLs (e.g. "Reconnaissance (https://...)")
    cleaned = re.sub(r'\s*\(https?://[^)]+\)', '', field)
    # Split by comma
    return [x.strip() for x in cleaned.split(',') if x.strip()]

def migrate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    init_db(cursor)
    
    print("Migrating data...")
    
    # Read CSV
    with open(CSV_PATH, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        # Debug: print fieldnames
        if reader.fieldnames:
             print(f"CSV Headers: {reader.fieldnames}")
        
        for row in reader:
            title = row['Vector']
            description = row['Description']
            
            # Skip empty rows (blank lines in CSV)
            if not title or not title.strip():
                continue
            
            # Insert Technique
            cursor.execute("INSERT INTO techniques (title, description) VALUES (?, ?)", (title, description))
            tech_id = cursor.lastrowid
            
            # Accumulate metadata for FTS
            metadata_text = []
            
            # Process Categories
            for cat in clean_csv_field(row['Security Domains']):
                cat_id = get_or_create(cursor, 'categories', cat)
                if cat_id:
                    cursor.execute("INSERT INTO technique_categories VALUES (?, ?)", (tech_id, cat_id))
                    metadata_text.append(cat)
            
            # Process Platforms
            for plat in clean_csv_field(row['OS']):
                plat_id = get_or_create(cursor, 'platforms', plat)
                if plat_id:
                    cursor.execute("INSERT INTO technique_platforms VALUES (?, ?)", (tech_id, plat_id))
                    metadata_text.append(plat)
                    
            # Process Technologies
            for tech in clean_csv_field(row['Target_Technology']):
                tech_id_tech = get_or_create(cursor, 'technologies', tech)
                if tech_id_tech:
                    cursor.execute("INSERT INTO technique_technologies VALUES (?, ?)", (tech_id, tech_id_tech))
                    metadata_text.append(tech)

            # Helper to find markdown file
            # ... (find file logic) ...
            
            # Normalize title for filename matching 
            # Replace special chars with space, then collapse multiple spaces to single space
            # Added more chars: < > " ' ? * | \
            safe_title = re.sub(r'[/:<>"\'?*|\\]', ' ', title)
            safe_title = re.sub(r'\s+', ' ', safe_title).strip().lower()
            
            found_file = None
            best_match_len = 0
            
            # Helper to clean filename: remove hash and extension, normalize
            def clean_filename(fname):
                # Remove extension
                name = os.path.splitext(fname)[0]
                # Remove hash (last 32 chars if hex) - simplified assuming space + 32 chars
                name = re.sub(r' [a-f0-9]{32}$', '', name)
                # Normalize
                return re.sub(r'\s+', ' ', name).strip().lower()

            for fname in os.listdir(MARKDOWN_DIR):
                if not fname.endswith('.md'):
                    continue
                    
                norm_fname = clean_filename(fname)
                
                # Check 1: Filename starts with Title (Good for untruncated files)
                # safe_title: "find files..."
                # norm_fname: "find files..."
                if norm_fname.startswith(safe_title):
                    found_file = os.path.join(MARKDOWN_DIR, fname)
                    break # Exact/Prefix match is best, stop immediately
                
                # Check 2: Title starts with Filename (Good for truncated files)
                # safe_title: "gau create ... run dalfox"
                # norm_fname: "gau create ... for pot"
                if len(norm_fname) > 10 and safe_title.startswith(norm_fname):
                    # We want the *longest* match to be safe
                    if len(norm_fname) > best_match_len:
                        best_match_len = len(norm_fname)
                        found_file = os.path.join(MARKDOWN_DIR, fname)
            
            # Start FTS content with Description + Metadata
            content_for_fts = (description or "") + " " + " ".join(metadata_text)
            
            if found_file:
                snippets = parse_markdown(found_file)
                for snip in snippets:
                    cursor.execute("INSERT INTO snippets (technique_id, language, content) VALUES (?, ?, ?)", 
                                   (tech_id, snip['language'], snip['content']))
                    content_for_fts += " " + snip['content']
            
            # Update FTS
            cursor.execute("INSERT INTO techniques_fts (title, description, content, technique_id) VALUES (?, ?, ?, ?)",
                           (title, description, content_for_fts, tech_id))

    conn.commit()
    conn.close()
    print("Migration complete!")

if __name__ == "__main__":
    migrate()
