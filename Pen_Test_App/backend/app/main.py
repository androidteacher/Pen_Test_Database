from fastapi import FastAPI, Depends, HTTPException, status, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import FileResponse
from typing import List, Optional
from .database import get_db, get_db_connection, DB_PATH
from .models import SearchResult, TechniqueDetail, Snippet, TechniqueCreate, MetaItem
from .search_logic import search_techniques_fts
from .auth import Token, create_access_token, get_current_user, get_password_hash, verify_password, User
import sqlite3
import shutil
import os

app = FastAPI(title="Pen Test Database API")

# Startup: Initialize DB and Seed Admin
@app.on_event("startup")
def startup_db():
    conn = get_db_connection()
    try:
        # Create Users Table
        with open("user_schema.sql", "r") as f:
            schema = f.read()
        conn.executescript(schema)
        
        # Seed Admin
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", ("admin",))
        user = cursor.fetchone()
        if not user:
            print("Seeding admin user...")
            hashed_pw = get_password_hash("admin")
            cursor.execute("INSERT INTO users (username, hashed_password, is_superuser) VALUES (?, ?, ?)", 
                           ("admin", hashed_pw, 1))
            conn.commit()
    except Exception as e:
        print(f"Startup error: {e}")
    finally:
        conn.close()

# Allow CORS for development (Frontend on different port)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, lock this down
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search", response_model=List[SearchResult])
def search(q: str = "", limit: int = 100, db: sqlite3.Connection = Depends(get_db)):
    """
    Search techniques. If q is empty, returns recent/all techniques.
    Includes Categories and Platforms for table view.
    """
    cursor = db.cursor()
    
    ids_scores = {} # map id -> rank/score
    
    if q:
        # 1. Perform FTS Search to get IDs
        fts_results = search_techniques_fts(db, q, limit)
        # fts_results is list of tuples: (id, title, description, snippet, rank)
        if not fts_results:
            return []
        
        # Extract IDs and preserve rank/snippet
        for r in fts_results:
             # r[0] is id. 
             # Note: search_techniques_fts returns (id, title, desc, snippet, rank)
             ids_scores[r[0]] = {
                 'snippet': r[3],
                 'rank': r[4]
             }
        
        if not ids_scores:
            return []
            
        placeholders = ','.join('?' for _ in ids_scores)
        where_clause = f"WHERE t.id IN ({placeholders})"
        params = list(ids_scores.keys())
    else:
        # No query, return all (up to limit)
        where_clause = ""
        params = []
        
    # 2. Fetch Metadata (Categories, Platforms) via aggregation
    # We use MAX(t.title) etc because of GROUP BY t.id
    sql = f"""
        SELECT 
            t.id, 
            t.title, 
            t.description,
            t.summary,
            GROUP_CONCAT(DISTINCT c.name) as category_names,
            GROUP_CONCAT(DISTINCT p.name) as platform_names
        FROM techniques t
        LEFT JOIN technique_categories tc ON t.id = tc.technique_id
        LEFT JOIN categories c ON tc.category_id = c.id
        LEFT JOIN technique_platforms tp ON t.id = tp.technique_id
        LEFT JOIN platforms p ON tp.platform_id = p.id
        {where_clause}
        GROUP BY t.id
    """
    
    if not q:
        sql += " ORDER BY t.title ASC" # Default sort
        if limit and limit > 0:
             sql += f" LIMIT {limit}"
    
    cursor.execute(sql, params)
    rows = cursor.fetchall()
    
    response = []
    for row in rows:
        t_id = row[0]
        t_title = row[1]
        t_desc = row[2]
        t_summary = row[3]
        cats = row[4].split(',') if row[4] else []
        plats = row[5].split(',') if row[5] else []
        
        # mix in FTS data if it exists
        snippet = None
        rank = 0.0
        if q and t_id in ids_scores:
            snippet = ids_scores[t_id]['snippet']
            rank = ids_scores[t_id]['rank']
        elif not q:
             # Just truncate description for snippet if no query
             snippet = (t_desc[:100] + "...") if t_desc else ""
        
        response.append(SearchResult(
            id=t_id,
            title=t_title,
            description=t_desc or "",
            summary=t_summary or "",
            categories=cats,
            platforms=plats,
            snippet_content=snippet,
            rank=rank
        ))
        
    # If search, re-sort by rank (since SQL IN clause loses order unless complicated)
    if q:
        response.sort(key=lambda x: x.rank)
        
    return response

@app.get("/technique/{tech_id}", response_model=TechniqueDetail)
def get_technique(tech_id: int, db: sqlite3.Connection = Depends(get_db)):
    """
    Get full details for a technique including categorized metadata and code snippets.
    """
    cursor = db.cursor()
    
    # 1. Fetch main technique data
    cursor.execute("SELECT * FROM techniques WHERE id = ?", (tech_id,))
    row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Technique not found")
        
    tech = dict(row)
    
    # 2. Fetch joined data (Categories, Platforms, Technologies)
    def fetch_names(target_table, join_table, fk_column):
        cursor.execute(f"""
            SELECT t.name FROM {target_table} t
            JOIN {join_table} jt ON t.id = jt.{fk_column}
            WHERE jt.technique_id = ?
        """, (tech_id,))
        return [r[0] for r in cursor.fetchall()]

    categories = fetch_names('categories', 'technique_categories', 'category_id')
    platforms = fetch_names('platforms', 'technique_platforms', 'platform_id')
    technologies = fetch_names('technologies', 'technique_technologies', 'technology_id')
    
    # 3. Fetch Snippets
    cursor.execute("SELECT language, content FROM snippets WHERE technique_id = ?", (tech_id,))
    snippets = [Snippet(language=r[0], content=r[1]) for r in cursor.fetchall()]
    
    return TechniqueDetail(
        id=tech['id'],
        title=tech['title'],
        description=tech['description'],
        created_at=tech['created_at'],
        updated_at=tech['updated_at'],
        categories=categories,
        platforms=platforms,
        technologies=technologies,
        snippets=snippets
    )

@app.get("/health")
def health():
    return {"status": "ok"}

# --- Auth Endpoints ---

@app.post("/auth/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (form_data.username,))
    user = cursor.fetchone()
    conn.close()

    if not user or not verify_password(form_data.password, user['hashed_password']):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": user['username']})
    return {"access_token": access_token, "token_type": "bearer"}

# --- Admin Endpoints ---

@app.get("/admin/backup")
async def backup_database(current_user: User = Depends(get_current_user)):
    if not os.path.exists(DB_PATH):
        raise HTTPException(status_code=404, detail="Database file not found")
    return FileResponse(path=DB_PATH, filename="pen_test_backup.db", media_type='application/octet-stream')

@app.post("/admin/restore")
async def restore_database(file: UploadFile = File(...), current_user: User = Depends(get_current_user)):
    try:
        # Save uploaded file to temp path then overwrite
        temp_path = f"{DB_PATH}.restore"
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        # Verify it's a valid sqlite db (basic check)
        try:
            test_conn = sqlite3.connect(temp_path)
            test_conn.cursor().execute("SELECT count(*) FROM sqlite_master")
            test_conn.close()
        except sqlite3.Error:
            if os.path.exists(temp_path):
                os.remove(temp_path)
            raise HTTPException(status_code=400, detail="Invalid SQLite file")

        # Overwrite content
        shutil.move(temp_path, DB_PATH)
        return {"status": "Database restored successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Restore failed: {str(e)}")

# --- Meta Endpoints ---

@app.get("/meta/categories", response_model=List[MetaItem])
def get_categories(db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM categories ORDER BY name")
    return [MetaItem(id=row[0], name=row[1]) for row in cursor.fetchall()]

@app.get("/meta/platforms", response_model=List[MetaItem])
def get_platforms(db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM platforms ORDER BY name")
    return [MetaItem(id=row[0], name=row[1]) for row in cursor.fetchall()]

# --- Create Endpoint ---

@app.post("/technique", status_code=status.HTTP_201_CREATED)
def create_technique(technique: TechniqueCreate, current_user: User = Depends(get_current_user), db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    try:
        # 1. Insert Technique
        cursor.execute("""
            INSERT INTO techniques (title, description, summary, created_at, updated_at) 
            VALUES (?, ?, ?, datetime('now'), datetime('now'))
        """, (technique.title, technique.description, technique.summary))
        
        new_id = cursor.lastrowid
        
        # 2. Insert Categories
        if technique.category_ids:
            cursor.executemany(
                "INSERT INTO technique_categories (technique_id, category_id) VALUES (?, ?)",
                [(new_id, cid) for cid in technique.category_ids]
            )
            
        # 3. Insert Platforms
        if technique.platform_ids:
            cursor.executemany(
                "INSERT INTO technique_platforms (technique_id, platform_id) VALUES (?, ?)",
                [(new_id, pid) for pid in technique.platform_ids]
            )
            
        db.commit()
        return {"id": new_id, "message": "Technique created successfully"}
    except sqlite3.Error as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/technique/{technique_id}")
def update_technique(technique_id: int, technique: TechniqueCreate, current_user: User = Depends(get_current_user), db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    try:
        # Check if exists
        cursor.execute("SELECT id FROM techniques WHERE id = ?", (technique_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Technique not found")

        # 1. Update Technique
        cursor.execute("""
            UPDATE techniques 
            SET title = ?, description = ?, summary = ?, updated_at = datetime('now')
            WHERE id = ?
        """, (technique.title, technique.description, technique.summary, technique_id))

        # 2. Update Categories (Delete all, then Insert new)
        cursor.execute("DELETE FROM technique_categories WHERE technique_id = ?", (technique_id,))
        if technique.category_ids:
            cursor.executemany(
                "INSERT INTO technique_categories (technique_id, category_id) VALUES (?, ?)",
                [(technique_id, cid) for cid in technique.category_ids]
            )

        # 3. Update Platforms (Delete all, then Insert new)
        cursor.execute("DELETE FROM technique_platforms WHERE technique_id = ?", (technique_id,))
        if technique.platform_ids:
            cursor.executemany(
                "INSERT INTO technique_platforms (technique_id, platform_id) VALUES (?, ?)",
                [(technique_id, pid) for pid in technique.platform_ids]
            )
        
        db.commit()
        return {"message": "Technique updated successfully"}
    except sqlite3.Error as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/technique/{technique_id}")
def delete_technique(technique_id: int, current_user: User = Depends(get_current_user), db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    try:
        # Check if exists
        cursor.execute("SELECT id FROM techniques WHERE id = ?", (technique_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Technique not found")

        # Cascading deletes (manually for safety/compatibility)
        cursor.execute("DELETE FROM technique_categories WHERE technique_id = ?", (technique_id,))
        cursor.execute("DELETE FROM technique_platforms WHERE technique_id = ?", (technique_id,))
        cursor.execute("DELETE FROM techniques WHERE id = ?", (technique_id,))
        
        # Trigger 'techniques_ad' should handle FTS deletion automatically
        
        db.commit()
        return {"message": "Technique deleted successfully"}
    except sqlite3.Error as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

