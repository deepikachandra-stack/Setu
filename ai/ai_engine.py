def understand_service(user_input):
    text = user_input.lower()

    if "income" in text:
        return "income_certificate"

    if "birth" in text:
        return "birth_certificate"

    return None