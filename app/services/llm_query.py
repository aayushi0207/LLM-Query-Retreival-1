import google.generativeai as genai
from app.core.config import GEMINI_API_KEY


# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

def run_llm(vector_store, question):
    # Retrieve top documents
    docs = vector_store.similarity_search(question, k=5)
    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
Instructions:
1. You are an expert Q&A system for insurance policies.
2. Answer the user's QUESTION based ONLY on the provided POLICY CONTENT.
3. Your answer must be concise and directly extracted from the text.
4. Do not add any extra phrases like "According to the policy..." or "The policy states...".

POLICY CONTENT:
---
{context}
---

QUESTION: {question}

ANSWER:
"""
    response = model.generate_content(prompt)
    return response.text.strip(), docs