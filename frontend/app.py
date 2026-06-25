import streamlit as st
import requests

st.title("DevPilot AI")

if st.button("Connect to Backend"):
    response = requests.get("http://127.0.0.1:8000/")

    if response.status_code == 200:
        data = response.json()
        st.success(data["message"])
    else:
        st.error("Failed to connect to backend")