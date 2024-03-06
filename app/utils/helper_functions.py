def chunk_text(text, chunk_size=200):
    '''
    Function takes a long text and divides it into smaller chunks while ensuring that each chunk does not exceed the specified size limit
    '''
    sentences = text.split(". ")
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= chunk_size: # checks if the chunk size is within the specified chunk size limit
            current_chunk += sentence + ". " # adds the current sentence with a period and space to the current_chunk
        else:
            chunks.append(current_chunk)
            current_chunk = sentence + ". "   

    if current_chunk: # checks to see if there are any other remaining contents after the loop
        chunks.append(current_chunk)

    return chunks     
