import logging

logging.basicConfig(level=logging.DEBUG)

PROMPT_LIMIT = 3750


def chunk_text(text, chunk_size=200):
    '''
    Function takes a long text and divides it into smaller chunks while ensuring that each chunk does not exceed the specified size limit
    '''
    logging.debug(f"chunking text of size {len(text)}")
    sentences = text.split(". ")
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        logging.debug(f"chunking sentence length {len(sentence)}")
        # checks if the chunk size is within the specified chunk size limit
        if len(current_chunk) + len(sentence) <= chunk_size:
            # adds the current sentence with a period and space to the current_chunk
            current_chunk += sentence + ". "
            logging.debug(f"current chunk length {len(current_chunk)}")
        else:
            chunks.append(current_chunk)
            current_chunk = sentence + ". "
            logging.debug(f"current chunk length {len(current_chunk)}")
    if current_chunk:  # checks to see if there are any other remaining contents after the loop
        chunks.append(current_chunk)
    logging.debug(f"final chunks size {len(chunks)}")

    return chunks


def build_prompt(query, context_chunks):
    '''
    This function creates a prompt for the question-answer task based on the context and question(query).
    The inputs to this function are:
    1. query - User prompted question
    2. context_chunks - list of texts chunks relevant to the question
    '''
    prompt_start = (
        "Answer the question based on the context below. If you don't know the answer based on the context provided below, respond with 'I apologise, I am not able to provide an answer at this time' instead of making up an answer. Return the answer to the question, don't add anything else. Don't start your response with the phrase 'Answer:'. Make sure your response is in markdown format\n\n" +
        "Context:\n"
    )

    prompt_end = (
        f"\n\nQuestion: {query}\nAnswer:"

    )

    prompt = ""

    for i in range(1, len(context_chunks)):
        # iterates through the context chunks to determine how much of the context can be included in the prompt without exceeding the limit.
        if len("\n\n--\n\n".join(context_chunks[:i])) >= PROMPT_LIMIT:
            # when the limit is reached/exceeded, prompt is constructed using the selected context chunks
            prompt = (
                prompt_start +
                "\n\n--\n\n".join(context_chunks[:i-1]) +
                prompt_end
            )
            break
        elif i == len(context_chunks)-1:
            # If the limit is not reached even after including all the context chunks, then the entire context is used to create the prompt
            prompt = (
                prompt_start +
                "\n\n--\n\n".join(context_chunks) +
                prompt_end
            )

    return prompt
