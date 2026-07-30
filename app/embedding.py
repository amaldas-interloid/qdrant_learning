from sentence_transformers import SentenceTransformer
from config import MODEL_NAME
model= SentenceTransformer(MODEL_NAME)

def generate_embeddings(documents):
    
    """
    Generate embeddings for documents.
    """
    return model.encode(documents)

def generate_query_embedding(query):
    """
    Generate embedding for user query.
    """
    return model.encode(query)  