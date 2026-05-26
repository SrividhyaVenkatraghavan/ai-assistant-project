import streamlit as st
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

client = InferenceClient(
   model="Qwen/Qwen2.5-72B-Instruct",
    token=os.getenv("HF_TOKEN")
)

st.set_page_config(page_title="OSS Assistant", page_icon="🧠")
st.title("🧠 OSS AI Assistant (Mistral via HuggingFace)")

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

    response = client.chat_completion(
        messages=[{"role": "system", "content": "You are a helpful assistant."}] + history,
        max_tokens=512,
        temperature=0.7
    )

    reply = response.choices[0].message.content

    with st.chat_message("assistant"):
        st.markdown(reply)
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })
