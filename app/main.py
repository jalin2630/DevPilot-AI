from fastapi import FastAPI
from app.models.chat import ChatRequest
from app.services.chat_service import ChatService

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Welcome to DevPilot AI!"
    }

@app.post("/chat")
def chat(request: ChatRequest):

    reply = ChatService.get_response(
        request.message
    )

    return {
        "reply": reply
    }