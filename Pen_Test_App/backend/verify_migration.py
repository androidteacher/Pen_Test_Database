import csv
import os
import re

CSV_PATH = "../../1/Pen Test Database 1434c8e52376809da4d5d2b49e01cce9.csv"
MARKDOWN_DIR = "../../1/Pen Test Database"

def normalize(text):
    text = re.sub(r'[/:<>"\'?*|\\]', ' ', text)
    return re.sub(r'\s+', ' ', text).strip().lower()

def verify():
    # 1. Load Real Filenames
    real_files = os.listdir(MARKDOWN_DIR)
    normalized_files = {} 
    for f in real_files:
        if not f.endswith('.md'): continue
        # keys are normalized filenames without the hash id at the end if possible
        # But for now let's just keep the full normalized name
        norm_name = normalize(f)
        normalized_files[norm_name] = f

    print(f"Loaded {len(normalized_files)} markdown files.")

    # 2. Check CSV
    matches = 0
    failures = 0
    
    with open(CSV_PATH, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            title = row['Vector']
            if not title or not title.strip(): continue
            
            safe_title = normalize(title)
            
            # Logic from migration_script.py
            found_file = None
            best_match_len = 0
            
            # Helper to clean filename: remove hash and extension, normalize
            def clean_filename(fname):
                name = os.path.splitext(fname)[0]
                name = re.sub(r' [a-f0-9]{32}$', '', name)
                return re.sub(r'\s+', ' ', name).strip().lower()

            for fname in os.listdir(MARKDOWN_DIR):
                if not fname.endswith('.md'): continue
                    
                norm_fname = clean_filename(fname)
                
                # Check 1: Filename starts with Title (Good for untruncated files)
                if norm_fname.startswith(safe_title):
                    found_file = fname
                    break 
                
                # Check 2: Title starts with Filename (Good for truncated files)
                if len(norm_fname) > 10 and safe_title.startswith(norm_fname):
                    if len(norm_fname) > best_match_len:
                        best_match_len = len(norm_fname)
                        found_file = fname
            
            if found_file:
                matches += 1
            else:
                failures += 1
                print(f"[FAIL] Could not match: '{title}'")

    print(f"\nSummary: {matches} Matched, {failures} Failed.")

if __name__ == "__main__":
    verify()
