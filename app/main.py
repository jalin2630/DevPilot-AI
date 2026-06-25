from fastapi import FastAPI
from app.models.chat import ChatRequest

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "message": "Welcome to DevPilot AI!"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "reply": f"You said: {request.message}"
    }