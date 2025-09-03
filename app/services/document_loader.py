# from langchain_community.document_loaders import UnstructuredURLLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from app.core.config import CHUNK_SIZE, CHUNK_OVERLAP

# def load_and_chunk(url: str):
#     loader = UnstructuredURLLoader(urls=[url])
#     documents = loader.load()
#     print(f"📄 Loaded {len(documents)} documents")

#     splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
#     chunks = splitter.split_documents(documents)
#     print(f"🧩 Split into {len(chunks)} chunks")

#     return chunks


import requests
import io
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from app.core.config import CHUNK_SIZE, CHUNK_OVERLAP

def load_and_chunk(url: str):
    """
    Downloads a PDF from a URL, extracts its text, and splits it into chunks.
    This version uses requests and pypdf to avoid heavy dependencies.
    """
    try:
        # Step 1: Download the PDF content from the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Step 2: Read the PDF content from memory
        pdf_file = io.BytesIO(response.content)
        reader = PdfReader(pdf_file)

        # Step 3: Extract text from all pages
        full_text = ""
        for page in reader.pages:
            full_text += page.extract_text() or ""
        
        if not full_text.strip():
            print("⚠️ Warning: No text could be extracted from the PDF.")
            return []

        # Step 4: Create a single LangChain Document
        # The text splitter will handle breaking this down.
        documents = [Document(page_content=full_text, metadata={"source": url})]
        print(f"📄 Loaded text from 1 document")

        # Step 5: Split the document into chunks
        splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
        chunks = splitter.split_documents(documents)
        print(f"🧩 Split into {len(chunks)} chunks")

        return chunks

    except requests.exceptions.RequestException as e:
        print(f"❌ Error downloading file from {url}: {e}")
        return []
    except Exception as e:
        print(f"❌ An error occurred while processing the PDF: {e}")
        return []