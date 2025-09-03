from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS # Updated import
import os
from pydantic import SecretStr

google_api_key = os.getenv("GEMINI_API_KEY")
if not google_api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=SecretStr(google_api_key)
)


def create_vector_store(chunks):
    vector_store = FAISS.from_documents(chunks, embedding_model)
    print(f"🔢 Creating embeddings for {len(chunks)} chunks")
    return vector_store
