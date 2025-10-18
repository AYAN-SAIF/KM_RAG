# RAG_frontend.py

import streamlit as st
from pathlib import Path
from rag_copy import setup_pipeline_and_query, PDF_PATH  # change this to your backend filename

st.set_page_config(page_title=" Kausar Medico Chatbot", layout="centered")

st.title("Welcome to Kausar Medico")
st.caption("Ask questions about Kausar Medico")

# initialize session
if "messages" not in st.session_state:
    st.session_state.messages = []

# chat display
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# user input
user_input = st.chat_input(" Ask your question here")

if user_input:
    # display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # generate AI response
    with st.chat_message("assistant"):
        with st.spinner(" Thinking..."):
            try:
                response = setup_pipeline_and_query(PDF_PATH, user_input)
            except Exception as e:
                response = f"⚠️ Error: {e}"

        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
