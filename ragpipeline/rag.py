#data ingestion 
from langchain_community.document_loaders import TextLoader
loader=TextLoader("speech.txt")
text=loader.load()
text