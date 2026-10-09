def check_documents(required_documents, user_documents):
    missing_documents = []

    user_documents_lower = [
        document.lower().strip()
        for document in user_documents
    ]

    for required in required_documents:
        if required.lower().strip() not in user_documents_lower:
            missing_documents.append(required)

    return missing_documents