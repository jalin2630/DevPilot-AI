import streamlit as st
import requests

st.title("DevPilot AI")

user_message = st.text_input("Enter your message")

if st.button("Send"):

    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json={
            "message": user_message
        }
    )

    data = response.json()

    st.success(data["reply"])