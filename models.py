from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()#its for the env file
model=ChatGroq(model="llama-3.3-70b-versatile",temperature=0.2) 
result=model.invoke("what is the capital of nepal?")
print(result.content)
