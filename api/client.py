import requests
import streamlit as st

def get_openai_response(input_text):
    response=requests.post("http://localhost:8081/essay/invoke",
    json={"input":{"topic":input_text}})
    return response.json()['output']['content']

def get_ollama_response(input_text):
    response=requests.post("http://localhost:8081/poem/invoke",
    json={"input":{"topic":input_text}})

    return response.json()['output']

#Stream lit
st.title("Langchain with multiple LLm models")
input_text=st.text_input("Write an essay topic:")
input_text1=st.text_input("Write an poem topic:",placeholder="I havent configured this  model it wont work")

if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))

