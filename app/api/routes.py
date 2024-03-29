import logging
from . import api_blueprint
from flask import request, jsonify
from app.services import openai_service, pinecone_service, scraping_service
from app.utils.helper_functions import chunk_text, build_prompt

PINECONE_INDEX_NAME = "index237"


@api_blueprint.route("/embed-and-store", methods=["POST"])
def embed_and_store():
    '''
    Function handles the following:
    1. Scraping the URL
    2. Embedding the texts
    3. Uploading to the vector database
    '''
    logging.basicConfig(level=logging.DEBUG)

    try:
        url = request.json["url"]
        logging.debug(f"Received URL: {url}")
        url_text = scraping_service.scrape_website(url)
        chunks = chunk_text(url_text)
        pinecone_service.embed_chunks_and_upload_to_pinecone(
            chunks, PINECONE_INDEX_NAME)
        response_json = {
            "message": "Chunks embedded and uploaded successfully to Pinecone"
        }

    except Exception as e:
        logging.error(f"Error processing request:{e}")
        response_json = {"error": "Failed to process request"}

    return jsonify(response_json)


@api_blueprint.route("/handle-query", methods=["POST"])
def handle_query():
    '''
    Function handles the following:
    1. Embedding the user's question
    2. Finding relevant context from the vector DB
    3. Building the prompt for the LLM
    4. Sending the prompt to the LLM's API to get an answer
    '''
    question = request.json["question"]
    context_chunks = pinecone_service.get_most_similar_chunks_for_query(
        question, PINECONE_INDEX_NAME)
    prompt = build_prompt(question, context_chunks)
    answer = openai_service.get_answer(prompt)

    return jsonify({"question": question, "answer": answer})
