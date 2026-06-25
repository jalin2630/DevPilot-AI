def generate_reply(message: str):
    message = message.lower()

    if "hello" in message:
        return "Hello! How can I help you today?"

    elif "your name" in message:
        return "I am DevPilot AI."

    elif "bye" in message:
        return "Goodbye! Have a great day."

    else:
        return f"You said: {message}"