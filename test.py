from ai.ai_engine import understand_service
from ai.requirement_checker import check_documents


def test_missing_income_proof():
    required = [
        "Identity proof",
        "Address proof",
        "Income proof"
    ]

    user_has = [
        "Identity proof",
        "Address proof"
    ]

    missing = check_documents(required, user_has)

    assert missing == ["Income proof"]
    print("Test 1 passed!")


def test_aadhaar_card():
    required = [
        "Identity proof",
        "Address proof"
    ]

    user_has = ["Aadhaar card"]

    missing = check_documents(required, user_has)

    assert missing == []
    print("Test 2 passed!")
def test_service_recognition():
    cases = {
        "I need an income certificate": "income_certificate",
        "Register my newborn baby": "birth_certificate",
        "I need a scholarship": "scholarship",
        "I need a caste certificate": "caste_certificate",
        "I need a ration card": "ration_card"
    }

    for message, expected in cases.items():
        actual = understand_service(message)
        assert actual == expected, f"{message}: got {actual}"

    print("Test 3 passed! All five services recognized.")

if __name__ == "__main__":
    test_missing_income_proof()
    test_service_recognition()
    test_aadhaar_card()