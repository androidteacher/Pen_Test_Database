import re
import sqlite3

def expand_query(cursor: sqlite3.Cursor, user_query: str) -> str:
    """
    Expands user query based on synonyms in search_terms table.
    Example: "rce" -> "Execution OR 'Command Injection'"
    """
    tokens = user_query.lower().split()
    expanded_parts = []
    
    for token in tokens:
        # Check for direct synonym
        cursor.execute("SELECT expanded_query FROM search_terms WHERE term = ?", (token,))
        row = cursor.fetchone()
        if row:
            # FTS5 uses double quotes for phrases, ensure synonyms are compatible
            # We assume expanded_query in DB also needs correction if it has single quotes
            expanded = row[0].replace("'", '"')
            expanded_parts.append(f"({expanded})")
        else:
            # Clean token for FTS (remove special chars that break syntax if needed)
            clean_token = re.sub(r'[^a-zA-Z0-9]', '', token)
            if clean_token:
                expanded_parts.append(clean_token)
    
    # Join with AND to ensure all parts are present (or their synonyms)
    if not expanded_parts:
        return ""
    
    return " AND ".join(expanded_parts)

def search_techniques_fts(conn: sqlite3.Connection, query: str, limit: int = 20):
    cursor = conn.cursor()
    
    # 1. Expand Query
    fts_query = expand_query(cursor, query)
    if not fts_query:
        return []

    # 2. Perform FTS Search
    # We join with the main techniques table to get the real ID (technique_id in FTS is UNINDEXED but stores the int)
    sql = """
        SELECT 
            t.id, 
            t.title, 
            t.description, 
            snippet(techniques_fts, 2, '<b>', '</b>', '...', 64) as snippet_content,
            techniques_fts.rank
        FROM techniques_fts
        JOIN techniques t ON t.id = techniques_fts.technique_id
        WHERE techniques_fts MATCH ?
        ORDER BY techniques_fts.rank
        LIMIT ?
    """
    
    cursor.execute(sql, (fts_query, limit))
    return cursor.fetchall()
