from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "DevPilot AI")
BOT_NAME = os.getenv("BOT_NAME", "DevPilot")
VERSION = os.getenv("VERSION", "1.0")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

print("Gemini Key Exists:", GEMINI_API_KEY is not None)
print("Gemini Key Prefix:", GEMINI_API_KEY[:8] if GEMINI_API_KEY else None)