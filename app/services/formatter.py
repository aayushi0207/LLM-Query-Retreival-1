from app.models.schema import Answer

def format_output(question, answer_text, source_docs):
    rationale = answer_text  # For simplicity, assuming same as answer
    sources = [doc.page_content for doc in source_docs]
    return Answer(question=question, answer=answer_text, rationale=rationale, source_clauses=sources)


