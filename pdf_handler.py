from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

class PDF_Handler():
    # Constructor
    def __init__(self, document_path: str, chunk_size=1000, chunk_overlap=50):
        self.document_path = document_path
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            is_separator_regex=False
        )
    
    # Fucntion for loading and creating the chunks of the document
    def load_docs(self):
        loader = PyPDFLoader(self.document_path)
        documents = loader.load()
        # print(f"Loaded {len(documents)} document(s)")
        chunks = []
        for doc in documents:
            text = doc.page_content
            chunk = self.text_splitter.create_documents([text])
            chunks.extend(chunk)
        # print(f"Created {len(chunks)} chunks")
        return chunks