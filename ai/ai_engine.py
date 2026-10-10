def understand_service(user_input):
    text = user_input.lower().strip()

    service_keywords = {
        "income_certificate": [
            "income certificate",
            "income proof",
            "salary proof",
            "family income",
            "family earnings"
        ],
        "birth_certificate": [
            "birth certificate",
            "birth registration",
            "newborn",
            "date of birth",
            "register my baby"
        ],
        "scholarship": [
            "scholarship",
            "student financial aid",
            "education funding",
            "student assistance"
        ],
        "caste_certificate": [
            "caste certificate",
            "caste proof",
            "community certificate"
        ],
        "ration_card": [
            "ration card",
            "food ration",
            "public distribution card",
            "add family member to ration card"
        ]
    }

    for service_id, keywords in service_keywords.items():
        if any(keyword in text for keyword in keywords):
            return service_id

    return None