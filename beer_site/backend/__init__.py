from flask import Blueprint, request, jsonify
from .model import process_document, initialize_conversation, create_hybrid_retriever

backend_bp = Blueprint("backend", __name__, static_folder="static",
                       static_url_path="/backend/static", url_prefix="/backend")

@backend_bp.route("/query_chat_with_beer", methods=["POST"])
def query_chat_with_beer():
    print("test")
    document_chunks = process_document("./beer_site/backend/static/docs/Verslag OC.pdf")
    qa_chain = initialize_conversation(create_hybrid_retriever(document_chunks)) 
    query = str(request.json.get("message"))
    return jsonify({"answer": qa_chain({"question": query})["answer"]})