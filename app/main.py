from fastapi import FastAPI
from app.core.config import APP_NAME
from app.services.chat_service import generate_reply
from app.models.chat import ChatRequest

app = FastAPI()


@app.post("/chat")
def chat(request: ChatRequest):

    reply = generate_reply(request.message)

    return {
        "reply": reply
    }