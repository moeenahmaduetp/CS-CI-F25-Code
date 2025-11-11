import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from vector_db_handler import Vector_DB_Handler

# Loading .env variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def call_llm(user_query: str):
    vector_db_instance = Vector_DB_Handler()
    reference_data = vector_db_instance.search_vectorDB(
        question=user_query
    )
    llm = ChatOpenAI(
        model="gemini-2.5-flash",
        temperature=0.2,
        openai_api_key=GEMINI_API_KEY,
        openai_api_base="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
    messages = [
        SystemMessage(content="You are a helpful assistant, response userquery in simple words based on the reference data."),
        HumanMessage(
            content=f"""UserQuestion: {user_query} and Reference Data: {reference_data}"""
        )
    ]
    print(f'LLM Response Is: {llm.invoke(messages).content}')


call_llm(user_query='hello, how are you?')