from fastapi import FastAPI, Request #1 import FastAPI
import cohere
from dotenv import load_dotenv
import os
from pydantic import BaseModel
#from langchain_cohere import ChatCohere
#from langchain_core.messages import HumanMessage, AIMessage, SystemMessage


load_dotenv()
api_key = os.getenv("COHERE_API_KEY")
co = cohere.Client(api_key)

app = FastAPI(
    title="AVA",  
    description="My first agent",
    version="1.0.0",
    openapi_tags=[{"name": "Agile, Versatile, Accesible", "description": "Virtual Assistant"}]) # 2 instancia app

class UserMessage(BaseModel):
    message : str


@app.post("/chat")
#async def chat(user_message : UserMessage):
    #response = co.generate(
        #model = 'command', 
        #prompt=user_message.message,
        #max_tokens=100
    #)
    #return {'response': response.generations}