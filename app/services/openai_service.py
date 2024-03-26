import os
import json
import requests
import logging

logging.basicConfig(level=logging.DEBUG)

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_EMBEDDING_MODEL = "text-embedding-ada-002"
LLM_MODEL = "gpt-3.5-turbo"


def get_embedding(chunk):
    url = "https://api.openai.com/v1/embeddings"
    headers = {
        "content-type": "application/json; charset=utf-8",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    data = {
        "model": OPENAI_EMBEDDING_MODEL,
        "input": chunk
    }
    logging.debug(f"embedding chunk: {data}")
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_json = response.json()
    logging.debug(f"response json: {response_json}")
    embedding = response_json["data"][0]["embedding"]
    logging.debug(f"embedding: {embedding}")

    return embedding


def get_answer(prompt):
    '''
    This function is designed to interact with the OpenAI Chat Completions API for generating 
    responses to prompts along with some context using a LLM.
    '''
    # Array contains a system message stating that the assistant is helpful
    message_arr = [
        {"role": "system", "content": "You are a helpful assistant"}]
    # appending user prompt to the array
    message_arr.append({"role": "user", "content": prompt})

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "content-type": "application/json; charset=utf-8",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    # constructing the payload
    data = {
        "model": LLM_MODEL,
        "messages": message_arr,
        "temperature": 1,  # controls the randomness of the generated text
        "max_tokens": 1000
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    response_json = response.json()
    completion = response_json["choices"][0]["message"]["content"]

    return completion
