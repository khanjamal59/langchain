from langchain_huggingface import HuggingFacePipeline, HuggingFaceEmbeddings        


embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
documents = ["This is a test document.", "This is another test document."]
embeddings_list = embeddings.embed_documents(documents) 
print(embeddings_list)
