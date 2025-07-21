from fastapi import FastAPI #1 import FastAPI

app = FastAPI(
    title="AVA",  
    description="My first agent",
    version="1.0.0",
    openapi_tags=[{"name": "example", "description": "An example tag"}]

) # 2 instancia app

@app.get("/")
async def root():
    return {"message": "Hello, Jose!"}