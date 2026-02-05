from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from .database import get_db
from .models import SearchResult, TechniqueDetail, Snippet
from .search_logic import search_techniques_fts
import sqlite3

app = FastAPI(title="Pen Test Database API")

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
        cats = row[3].split(',') if row[3] else []
        plats = row[4].split(',') if row[4] else []
        
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
