from pdf_handler import PDF_Handler
from vector_db_handler import Vector_DB_Handler
from llm_calling import call_llm
import logging

# python logging code
logging.basicConfig(
    level= logging.DEBUG,
    filename='app.log',
    # format= '[]'
)

# PDF Handler instance
logging.info("PDF handler already done")
# pdf_handler_instance = PDF_Handler(
#     document_path='./sample_data.pdf'
# )
# chunks = pdf_handler_instance.load_docs()

# VectorDB instance
logging.info('creating the vectordb instance')
vector_db_instance = Vector_DB_Handler()
# vector_db_instance.loading_to_vectorDB(chunks)

# print(vector_db_instance.search_vectorDB(question='hydrogen is?'))
# query = 'What is hydrogen?'
# logging.info('searching in the vector_db based on user query')
# reference_docs = vector_db_instance.search_vectorDB(question=query)
# logging.info('calling the llm with reference data based on user query')
# call_llm(
#     user_query = query,
#     reference_data=reference_docs
# )