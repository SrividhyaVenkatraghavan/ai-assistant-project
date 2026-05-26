import streamlit as st
import os
from groq import Groq

# Directly set API key path
env_path = r"C:\Users\HP\OneDrive\Desktop\ai-assistant-project\.env"

# Read .env file manually
with open(env_path) as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("#"):
            key, value = line.split("=", 1)
            os.environ[key.strip()] = value.strip()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

st.set_page_config(page_title="Frontier Assistant", page_icon="🤖")
st.title("🤖 Frontier AI Assistant (Llama via Groq)")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    history = [
        {"role": m["role"], "content": m["content"]}
        for m in st.session_state.messages
    ]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "system", "content": "You are a helpful assistant."}] + history
    )

    reply = response.choices[0].message.content

    with st.chat_message("assistant"):
        st.markdown(reply)
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })
