DOCUMENT_ALIASES = {
    "Identity proof": [
        "aadhaar",
        "aadhar",
        "aadhaar card",
        "pan card",
        "voter id",
        "passport"
    ],
    "Address proof": [
        "aadhaar",
        "aadhaar card",
        "aadhar",
        "voter id",
        "utility bill",
        "address certificate"
    ],
    "Income proof": [
        "salary slip",
        "income certificate",
        "salary certificate",
        "income proof"
    ]
}


def check_documents(required_documents, user_documents):
    missing_documents = []

    user_documents_lower = [
        document.lower().strip()
        for document in user_documents
    ]

    for required in required_documents:
        required_lower = required.lower().strip()

        aliases = DOCUMENT_ALIASES.get(required, [])

        found = any(
            document == required_lower
            or document in [
                alias.lower() for alias in aliases
            ]
            for document in user_documents_lower
        )

        if not found:
            missing_documents.append(required)

    return missing_documents