

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("ls__4bbef910784e41889d4bcf7604a10781")

#prompt template 
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are  helpful emotionally intelligent assistant please answer the user queries")
        ("the following are the {emotion} and this is the questions:{question}")
    ]
)


# ollama LLAma2 LLm 
llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser
if input_text:
    st.write(chain.invoke({"question":input_text}))