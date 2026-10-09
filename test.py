from ai.requirement_checker import check_documents

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

print(missing)