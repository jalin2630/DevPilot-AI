from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "DevPilot AI")
BOT_NAME = os.getenv("BOT_NAME", "DevPilot")
VERSION = os.getenv("VERSION", "1.0")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")