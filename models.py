from langchain_core.messages import SystemMessage, HumanMessage,AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

model=ChatGroq(model="llama-3.3-70b-versatile")

messages=[
    SystemMessage(content="You are a helpful assistant that writes short and sweet quotes for birthday cards."),
    HumanMessage(content="write a short and sweet quotes for a birthday card")  
]

result=model.invoke(messages)
messages.append(AIMessage(content=result.content))

print("AI response:", result.content)
