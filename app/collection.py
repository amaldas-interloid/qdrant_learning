
from client import client
from config import COLLECTION_NAME,VECTOR_SIZE
from qdrant_client.models import VectorParams,Distance
def create_collection():
    client.create_collection(
        collection_name= COLLECTION_NAME,
        vectors_config= VectorParams(
            size= VECTOR_SIZE,
            distance= Distance.COSINE,
        ),      
    )
    