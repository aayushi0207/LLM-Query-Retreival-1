from pydantic import BaseModel
from typing import List

class QueryInput(BaseModel):
    documents: str
    questions: List[str]

class Answer(BaseModel):
    question: str
    answer: str
    rationale: str
    source_clauses: List[str]

class QueryResponse(BaseModel):
    answers: List[Answer]
