from app.services.ai_service import generate_ai_reply


def generate_reply(message: str):
    return generate_ai_reply(message)