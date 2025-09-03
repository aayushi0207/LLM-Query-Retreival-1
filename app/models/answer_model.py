class Document:
    def __init__(self, page_content):
        self.page_content = page_content

class AnswerData:
    def __init__(self, question: str, answer: str, rationale: str, sources: list[Document]):
        self.question = question
        self.answer = answer
        self.rationale = rationale
        self.source_clauses = [doc.page_content for doc in sources]
