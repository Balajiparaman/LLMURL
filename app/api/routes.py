from . import api_blueprint

@api_blueprint.route("/embed-and-store", methods=["POST"])
def embed_and_store():
    '''
    Function handles the following:
    1. Scraping the URL
    2. Embedding the texts
    3. Uploading to the vector database
    '''
    pass

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