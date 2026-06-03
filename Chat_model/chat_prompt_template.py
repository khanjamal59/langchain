#chat promot template to dynamically insert or a list of messages at runtime 
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

chat_template=ChatPromptTemplate.from_messages([
    ('system', "You are a helpful {domain} assistant."),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', "Explain in the simple terms what is the {topic}")    
])
chat_history=[]
#loading chat history
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())
print(chat_history)
   
#creating the prompt
prompt =chat_template.invoke({'chat_history':chat_history,'domain':'cricket', 'topic':'Duckworth-Lewis method'}) 
#prompt=chat_template.invoke({'domain':'cricket', 'topic':'Duckworth-Lewis method'})
print(prompt)
