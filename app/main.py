from fastapi import FastAPI
from app.core.config import APP_NAME, VERSION
from app.models.chat import ChatRequest
from app.services.chat_service import generate_reply

app = FastAPI(
    title=APP_NAME,
    version=VERSION
)

@app.get("/")
def root():
    return {
        "message": f"Welcome to {APP_NAME}"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "version": VERSION
    }

@app.post("/chat")
def chat(request: ChatRequest):
    reply = generate_reply(request.message)
    return {
        "reply": reply
    }