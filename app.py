import streamlit as st
import google.generativeai as genai


st.title("welcome to Thatchan AI chat")

genai.configure(api_key="AIzaSyCnGfSjBFZ42AtjIJ7IlGCM3wSGjkzh7LI")  #to get api-key https://aistudio.google.com/app/apikey

text = st.text_input("enter your question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


if st.button("Click me"):
    response = chat.send_message(text)
    st.write(response.text)
