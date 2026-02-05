from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Snippet(BaseModel):
    language: str
    content: str

class TechniqueSummary(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    categories: List[str] = []
    platforms: List[str] = []

class TechniqueDetail(TechniqueSummary):
    technologies: List[str] = []
    snippets: List[Snippet] = []
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

class SearchResult(BaseModel):
    id: int
    title: str
    description: str
    categories: List[str] = []
    platforms: List[str] = []
    snippet_content: Optional[str] = None
    rank: float
