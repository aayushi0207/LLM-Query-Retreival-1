from app.services.document_loader import load_and_chunk
from app.services.embeddings import create_vector_store
from app.services.llm_query import run_llm
from app.services.formatter import format_output
from app.models.schema import QueryResponse

def process_queries(doc_url, questions):
    chunks = load_and_chunk(doc_url)
    vector_store = create_vector_store(chunks)

    answers = []
    for question in questions:
        answer_text, source_docs = run_llm(vector_store, question)
        answer = format_output(question, answer_text, source_docs)
        answers.append(answer)

    return {"answers": [answer.answer for answer in answers]}

