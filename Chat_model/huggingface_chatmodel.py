from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()   
usr_input=input("Enter your query")
llm=HuggingFaceEndpoint(repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
                    task="text-generation")
model=ChatHuggingFace(llm=llm)
result=model.invoke(usr_input)
print(result.content)
