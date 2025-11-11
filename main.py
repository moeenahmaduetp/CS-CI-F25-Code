from fastapi import FastAPI
from pydantic import BaseModel
from llm_calling import call_llm

app = FastAPI()

class chatBody(BaseModel):
    user_id: str
    user_query: str

@app.get('/')
def healty():
    return {
        'response': 'Healthy Condition'
    }

@app.post('/query')
def query(data: chatBody):
    response = call_llm(data.user_query)

    return {
        "response": response
    }