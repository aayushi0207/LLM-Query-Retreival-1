from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="LLM-Powered Query Retrieval System")
app.include_router(router)
