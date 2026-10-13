from flask import Flask, request, jsonify
from flask_cors import CORS
from ai.ai_engine import understand_service
from ai.process_loader import get_process
from ai.requirement_checker import check_documents


app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
    return "Setu backend is running!"

@app.route("/process")
def process():
    user_input = request.args.get("service", "")

    service = understand_service(user_input)

    if service is None:
        return jsonify({"error": "Service not understood"})

    process_data = get_process(service)

    return jsonify(process_data)

@app.route("/check-documents")
def check_documents_route():
    service = request.args.get("service", "")
    user_documents = request.args.getlist("document")

    service_id = understand_service(service)

    if service_id is None:
        return jsonify({"error": "Service not understood"})

    process_data = get_process(service_id)

    missing = check_documents(
        process_data["documents"],
        user_documents
    )

    return jsonify({
    "service": process_data["name"],
    "missing_documents": missing,
    "next_action": process_data["next_action"]
})


if __name__ == "__main__":
    app.run(debug=True)