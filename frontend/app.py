import streamlit as st
import requests

st.set_page_config(
    page_title="Luffy AI",
    page_icon="🏴‍☠️",
    layout="wide"
)

with st.sidebar:

    st.title("🏴‍☠️ Luffy AI")

    st.success("🟢 Connected")

    st.markdown("---")

    st.write("Version 1.1")

    st.write("Powered by Gemini")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("DevPilot AI")

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_message = st.chat_input("Message Luffy...")

if user_message:
    
    # Save the user's message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    # Send the message to FastAPI
    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json={
            "message": user_message
        }
    )

    data = response.json()

    # Save Luffy's reply
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": data["reply"]
        }
    )

    # Refresh the page to display new messages
    st.rerun()
