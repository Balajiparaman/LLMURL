import pinecone
from app.services.openai_service import get_embedding
import os

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")

pinecone.init(api_key=PINECONE_API_KEY)

EMBEDDING_DIM = 256


def embed_chunks_and_upload_to_pinecone(chunks, index_name):
    '''
    This function takes chunks(list of text chunks) and index_name(Pinecone index name) as inputs
    and uploads the embeddings along with the related metadata(chunk, ID) to the Pinecone Vector DB
    for efficient similarity search based on these embeddings.

    '''
    if index_name in pinecone.list_indexes():
        # if index name already exists within Pinecone, delete it.
        pinecone.delete_index(name=index_name)

    pinecone.create_index(name=index_name,
                          dimensions=EMBEDDING_DIM,
                          metric="cosine")

    index = pinecone.Index(index_name)

    embeddings_with_ids = []
    for i, chunk in enumerate(chunks):
        embedding = get_embedding(chunk)
        embeddings_with_ids.append((str(i), embedding, chunk))

    upserts = [(id, vec, {"chunk_text": chunk})
               for id, vec, chunk in embeddings_with_ids]
    index.upsert(vectors=upserts)


def get_most_similar_chunks_for_query():
    '''
    The function does the following actions:
    1. Embeds the question using openai embedding model via the get_embedding func
    2. Query the Pinecone DB to find the top 3 text chunks most similar to the question using cosine similarity algo
    3. Returns the texts of those chunks as a list
    '''
    question_embedding = get_embedding(query)
    index = pinecone.Index(index_name)
    query_results = index.query(
        question_embedding, top_k=3, include_metadata=True)
    context_chunks = [x["metadata"]["chunk_text"]
                      for x in query_results["matches"]]

    return context_chunks
