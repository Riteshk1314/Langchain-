from langchain_community.document_loaders import TextLoader

file_path = "speech.txt"
loader = TextLoader(file_path)

text_documents = loader.load()
print(text_documents)