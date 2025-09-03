def retrieve_clauses(vector_store, question, k=5):
    return vector_store.similarity_search(question, k=k)
