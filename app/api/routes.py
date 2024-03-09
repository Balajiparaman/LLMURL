from . import api_blueprint
from flask import requests, jsonify
from app.services import openai_service, pinecone_service, scraping_service
from app.utils.helper_functions import chunk_text

PINECONE_INDEX_NAME = 'index007'


@api_blueprint.route("/embed-and-store", methods=["POST"])
def embed_and_store():
    '''
    Function handles the following:
    1. Scraping the URL
    2. Embedding the texts
    3. Uploading to the vector database
    '''
    url = requests.json["url"]
    url_text = scraping_service.scrape_website(url)
    chunks = chunk_text(url_text)
    pinecone_service.embed_chunks_and_upload_to_pinecone(
        chunks, PINECONE_INDEX_NAME)
    response_json = {
        "message": "Chunks embedded and uploaded successfully to Pinecone"
    }

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
    pass
