@echo off
title Luffy AI

cd /d "C:\Users\moham\OneDrive\Desktop\DevPilot-AI"

call venv\Scripts\activate

start cmd /k "uvicorn app.main:app --reload"

timeout /t 3 >nul

start http://localhost:8501

streamlit run frontend\app.py