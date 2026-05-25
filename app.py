import streamlit as st
from chatbot import get_response

st.title("FAQ Chatbot")

question = st.text_input("Ask a Question")

if st.button("Send"):

    if question:

        answer = get_response(question)

        st.success(answer)
