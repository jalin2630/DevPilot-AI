from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = os.getenv("APP_NAME")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")