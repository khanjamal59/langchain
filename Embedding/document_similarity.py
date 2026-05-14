from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

# HuggingFace Embedding Model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "virat kohli is a great batsman virat kohli is a good captain",
    "mahendra singh dhoni is a great batsman mahendra singh dhoni is a good captain"
]

query = "tell me about virat kohli"

# Generate embeddings
document_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

# Calculate cosine similarity
similarity = cosine_similarity([query_embedding], document_embeddings)[0]

index, score=sorted((list(enumerate(similarity))), key=lambda x: x[1])[-1]
print(query)
print(documents[index])
print("similarity score:",score)
