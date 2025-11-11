import os
import shutil
from dotenv import load_dotenv
from uuid import uuid4
from langchain_chroma import Chroma
from typing import List
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Loading .env variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

class Vector_DB_Handler():
    # Constructor
    def __init__(self):
        self.embeddings = GoogleGenerativeAIEmbeddings(
            google_api_key=GEMINI_API_KEY,
            model = 'gemini-embedding-001'
        )
        self.vector_db = Chroma(
            collection_name = 'sample_data',
            embedding_function = self.embeddings,
            persist_directory = "./vectordb"
        )

    # Function for loading data to vector database
    def loading_to_vectorDB(self, documents: List[Document], fresh_load:bool = False):
        if fresh_load:
            self.delete_vectorDB()
        uuids = [str (uuid4()) for item in range(len(documents))]
        self.vector_db.add_documents(
            documents=documents,
            ids=uuids
        )

    # For deleting the existing vectordb
    def delete_vectorDB(path ='./vectordb'):
        if os.path.exists(path):
            shutil.rmtree(path)

 
    # Function for searching about data in vector database
    def search_vectorDB(self, question: str, no_of_docs_retreive:int=3):
        results = self.vector_db.similarity_search(
            question,
            no_of_docs_retreive
        )
        combined_result = ''
        for doc in results:
            combined_result += doc.page_content
            combined_result += '\n'

        return combined_result