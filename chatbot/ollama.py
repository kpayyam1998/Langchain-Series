from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
# whenever create chat bot above lib its realy very usefull
from langchain_core.output_parsers import StrOutputParser
# whenever import 3rd party llm that will be availbalbel  langchain_community
# ollama support all llama2 model and all github page 
from langchain_community.llms import ollama
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()


OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
#langsmith tracking
LANGCHAIN_API_KEY=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"


prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpfull assistent.please response for user queries"),
        ("user","Question:{question}")
    ]
)

#Streamlit
st.title("Langchain series")
input_text=st.text_input("Search the topic that you want")

# openai

llm=ollama(model="gpt-3.5-turbo-0301")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))



# If you want to use gamma model localled just install and 

# run command

# ollama run gemma to download  first time it will take time bocoz size will be 5gb