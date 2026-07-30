from qdrant_client.models import PointStruct
from client import client
from config import COLLECTION_NAME
def insert_documents(documents,embeddings):
    points= []
    for idx,(document,embedding) in enumerate(
        zip(documents,embeddings)
    ):
        points.append(
            PointStruct(
                id= idx,
                vector= embedding.tolist(),
                payload={
                    "text":document
                },
            )
        )
        
    client.upsert(
        collection_name= COLLECTION_NAME,
        points= points,
    )