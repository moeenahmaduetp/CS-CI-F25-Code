from pydantic import BaseModel
from datetime import datetime
from pymongo import MongoClient,ASCENDING
from langchain_core.messages import HumanMessage,AIMessage

class ChatMessage(BaseModel):
    user_id : str
    human: str
    assistant:str
    timestamp: datetime


client = MongoClient("mongodb://localhost:27017")

def save(data : ChatMessage):
    db = client["DB_DS"]["chats"]
    db.insert_one(data.model_dump())

def retrive(user_id:str):
    db = client["DB_DS"]["chats"]
    data = list(db.find(
        {"user_id": user_id}
    ).sort("timestamp",ASCENDING).limit(20))

    messages = []
    for item in data:
        messages.append(HumanMessage(item["human"]))
        messages.append(AIMessage(item["assistant"]))



    return messages