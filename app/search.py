from client import client
from config import COLLECTION_NAME


def search(query_vector, limit=3):

    return client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector.tolist(),
        limit=limit,
    )