import sqlite3
import os

DB_PATH = "pen_test.db"

def fix_fts():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("Dropping existing FTS triggers if any...")
    cursor.execute("DROP TRIGGER IF EXISTS techniques_ai")
    cursor.execute("DROP TRIGGER IF EXISTS techniques_au")
    cursor.execute("DROP TRIGGER IF EXISTS techniques_ad")
    
    print("Creating Triggers...")
    # Insert Trigger
    cursor.execute("""
    CREATE TRIGGER techniques_ai AFTER INSERT ON techniques BEGIN
      INSERT INTO techniques_fts(title, description, content, technique_id) 
      VALUES (new.title, new.description, new.description || ' ' || coalesce(new.summary, ''), new.id);
    END;
    """)
    
    # Update Trigger
    cursor.execute("""
    CREATE TRIGGER techniques_au AFTER UPDATE ON techniques BEGIN
      UPDATE techniques_fts SET 
        title = new.title, 
        description = new.description, 
        content = new.description || ' ' || coalesce(new.summary, '')
      WHERE technique_id = new.id;
    END;
    """)
    
    # Delete Trigger
    cursor.execute("""
    CREATE TRIGGER techniques_ad AFTER DELETE ON techniques BEGIN
      DELETE FROM techniques_fts WHERE technique_id = old.id;
    END;
    """)
    
    print("Re-indexing FTS...")
    cursor.execute("DELETE FROM techniques_fts")
    
    # Re-populate with joins for tags
    sql = """
    INSERT INTO techniques_fts (title, description, content, technique_id)
    SELECT 
        t.title, 
        t.description, 
        t.description || ' ' || IFNULL(t.summary, '') || ' ' || 
        IFNULL(GROUP_CONCAT(DISTINCT c.name), '') || ' ' || 
        IFNULL(GROUP_CONCAT(DISTINCT p.name), ''),
        t.id
    FROM techniques t
    LEFT JOIN technique_categories tc ON t.id = tc.technique_id
    LEFT JOIN categories c ON tc.category_id = c.id
    LEFT JOIN technique_platforms tp ON t.id = tp.technique_id
    LEFT JOIN platforms p ON tp.platform_id = p.id
    GROUP BY t.id
    """
    cursor.execute(sql)
    
    print(f"Re-indexed {cursor.rowcount} entries.")
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    fix_fts()
