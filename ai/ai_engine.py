def understand_service(user_input):
    text = user_input.lower().strip()

    income_keywords = [
        "income",
        "salary proof",
        "family earnings",
        "proof of income"
    ]

    birth_keywords = [
        "birth",
        "born",
        "newborn",
        "date of birth"
    ]

    if any(keyword in text for keyword in income_keywords):
        return "income_certificate"

    if any(keyword in text for keyword in birth_keywords):
        return "birth_certificate"

    return None