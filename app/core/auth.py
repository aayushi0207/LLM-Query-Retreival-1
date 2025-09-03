from app.core.config import API_TOKEN

def validate_token(header: str) -> bool:
    return header == f"Bearer {API_TOKEN}"
