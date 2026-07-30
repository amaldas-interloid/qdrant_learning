
from loader import load_documents
from embedding import generate_embeddings,generate_query_embedding
from insert import insert_documents
from search import search
def main():
    documents =load_documents("data/documents.txt")
    embeddings= generate_embeddings(documents)
    
    insert_documents(
        documents,
        embeddings,
    )
    
    while True:

        query = input(
            "\nAsk a Question (or type 'exit'): "
        )

        if query.lower() == "exit":
            break

        results = search(
            generate_query_embedding(query)
        )

        print("\nTop Results\n")

        for point in results.points:

            print(
                f"Score : {point.score:.4f}"
            )
            print(
                point.payload["text"]
            )
            print("-" * 40)


if __name__ == "__main__":
    main()
        
        
        
    