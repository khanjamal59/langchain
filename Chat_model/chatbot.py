from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()
#chat history


#model
model=ChatGroq(model="llama-3.3-70b-versatile")
chat_history=[
    SystemMessage(content="You are a helpful assistant that writes short and sweet quotes for birthday cards."),
]
while True:
    user_input=input("You:")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    
    model_response=model.invoke(chat_history) 
    
    chat_history.append(model_response.content)
    print("Ai:",model_response.content)
print("Chat history:", chat_history)
