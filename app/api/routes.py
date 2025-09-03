from fastapi import APIRouter, Header, HTTPException
from app.models.schema import QueryInput, QueryResponse
from app.core.auth import validate_token
from app.services.pipeline import process_queries

router = APIRouter()

@router.post("/api/v1/hackrx/run", response_model=QueryResponse)
def run_queries(payload: QueryInput, authorization: str = Header(...)):
    if not validate_token(authorization):
        raise HTTPException(status_code=401, detail="Unauthorized")
    return process_queries(payload.documents, payload.questions)
