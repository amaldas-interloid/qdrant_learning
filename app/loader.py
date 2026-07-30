def load_documents(file_path: str) -> list[str]:

    with open(file_path, "r") as file:
        documents = [
            line.strip()
            for line in file
            if line.strip()
        ]

    return documents