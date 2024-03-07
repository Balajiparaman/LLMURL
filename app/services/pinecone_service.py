import pinecone
from app.services.openai_service import get_embedding
import os

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")

pinecone.init(api_key=PINECONE_API_KEY)

EMBEDDING_DIM = 256


def embed_chunks_and_upload_to_pinecone(chunks, index_name):
    if index_name in pinecone.list_indexes():
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
