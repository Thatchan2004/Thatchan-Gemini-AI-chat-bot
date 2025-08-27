import streamlit as st
import google.generativeai as genai


st.title("welcome to Thatchan AI chat")

genai.configure(api_key="AIzaSyB9Fnu2d36mWJ1nL50R_wQJOK93zxCd7h8")  #to get api-key https://aistudio.google.com/app/apikey

text = st.text_input("enter your question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


if st.button("Click me"):
    response = chat.send_message(text)
    st.write(response.text)

