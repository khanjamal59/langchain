
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

#model
model=ChatGroq(model="llama-3.3-70b-versatile")
while True:
    user_input=input("You:")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    model_response=model.invoke(user_input) 
    print("Ai:",model_response.content)
