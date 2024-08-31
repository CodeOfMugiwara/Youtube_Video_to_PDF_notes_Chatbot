import openai


def split_text_into_chunks(text, max_chunk_size=1000):
    """Splits text into chunks of a specified maximum size."""
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        # Add the current word to the chunk
        current_chunk.append(word)
        # Join chunk into a single string and check its length
        if len(" ".join(current_chunk)) > max_chunk_size:
            # If chunk is too large, finalize the current chunk and start a new one
            chunks.append(" ".join(current_chunk[:-1]))
            current_chunk = [current_chunk[-1]]

    # Add the final chunk
    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks


def process_content(text, detail_level="simple"):
    """Process content in chunks to avoid exceeding token limits."""
    chunks = split_text_into_chunks(text)
    processed_chunks = []

    for chunk in chunks:
        if detail_level == "simple":
            prompt = f"""
Please generate well-structured notes from the following content. Use bold headings for each section and make the font size larger for the headings. For detailed information under each heading, use bullet points, with either dots or numbered lists, to clearly organize the content. Ensure the content is simplified but retains all key details:

{text}
"""

        else:
            prompt = f"""
Please create comprehensive, well-structured notes from the following content. Use bold and larger font sizes for headings, and break down each section into bullet points with either dots or numbered lists. Ensure that the content is detailed and includes explanations of key concepts, examples, and any relevant information, making it easy to understand for someone new to the topic:

{text}
"""

        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=2048
        )
        processed_chunks.append(response.choices[0].text.strip())

    # Combine all processed chunks into one result
    return "\n".join(processed_chunks)


def process_content(text, detail_level="simple"):
    max_chunk_size = 4097 - 1024  # leave room for completion
    chunks = split_text_into_chunks(text, max_chunk_size)
    responses = []

    for chunk in chunks:
        prompt = f"Summarize the following content: {chunk}"
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=1024
        )
        responses.append(response.choices[0].text.strip())

    return "\n".join(responses)


def summarize_content(text):
    """Summarize the content using OpenAI API."""
    prompt = f"Summarize the following content: {text}"
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=1024
    )
    return response.choices[0].text.strip()
