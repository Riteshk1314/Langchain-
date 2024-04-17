#creating a chatbot 
#usng open ai API or cloudy api
#callingi is easy but langchain has many modules but we have to use them accordinlgy to call apis
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv


os.environ["OPEN_API_KEY"]=os.getenv["OPENAI_API_KEY"]
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

#prompt template 
pormt=ChatPromptTemplate.from_messages(
    [
        ("system","you are  helpful assistant please answer the user queries")
        ("user","question:{question}")
    ]
)
##streamlit framework

st.title('Langchain Demo With LLAMA2 API')
input_text=st.text_input("Search the topic u want")

#openai llm
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))


# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_community.llms import Ollama
# import streamlit as st
# import os
# from dotenv import load_dotenv

# load_dotenv()

# os.environ["LANGCHAIN_TRACING_V2"]="true"
# os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# ## Prompt Template

# prompt=ChatPromptTemplate.from_messages(
#     [
#         ("system","You are a helpful assistant. Please response to the user queries"),
#         ("user","Question:{question}")
#     ]
# )
# ## streamlit framework

# st.title('Langchain Demo With LLAMA2 API')
# input_text=st.text_input("Search the topic u want")

# # ollama LLAma2 LLm 
# llm=Ollama(model="llama2")
# output_parser=StrOutputParser()
# chain=prompt|llm|output_parser

# if input_text:
#     st.write(chain.invoke({"question":input_text}))