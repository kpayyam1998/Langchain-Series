""""
We are going to convert model to api

# install blackbox AI extensions which is realy help to write code fast
"""
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai.chat_models import ChatOpenAI
from langserve import add_routes  #Byusing this we can add all the routes like (openai or llama 2)
import uvicorn
import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

#fastapi connection
app=FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server"
)

# api _path using Fast API
add_routes(
    app, #Fast api connection
    ChatOpenAI(),
    path="/openai"
)

# add_routes(
#     app, #Fast api connection
#     Ollama(),
#     path="/poem"
# )


model=ChatOpenAI()
#Ollama
llm=Ollama(model="llama2")

prompt1=ChatPromptTemplate.from_template("can you please write essay about{topic} in 100 words")
prompt2=ChatPromptTemplate.from_template("can you please write poem about{topic} in 50 words")
# We are going to pass our prompt to api_routes

add_routes(
    app,
    prompt1|model,
    path="/essay"
)
#ollama
add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8081)


# We are going to use this to our front end application