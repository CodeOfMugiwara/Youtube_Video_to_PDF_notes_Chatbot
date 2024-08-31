import openai
from url_handler import get_video_id
from transcription import get_transcript
from translation import translate_text_if_needed
from content_processing import process_content, summarize_content
from pdf_generator import generate_pdf


video_url = input("Enter YouTube video URL: ")
video_id = get_video_id(video_url)
print(f"Video ID: {video_id}")

transcript_text = get_transcript(video_id)
print(f"Transcript: {transcript_text}")

# Translate if the text is not in English
translated_text = translate_text_if_needed(transcript_text)
print(f"Translated Text: {translated_text}")

user_preference = input(
    "Do you want a simple explanation or detailed? (simple/detailed): ")

if user_preference == "simple":
    prompt = f"""
    Please generate well-structured notes from the following content. Use bold headings for each section and make the font size larger for the headings. For detailed information under each heading, use bullet points, with either dots or numbered lists, to clearly organize the content. Ensure the content is simplified but retains all key details:

    {translated_text}
    """
else:
    prompt = f"""
    Please create comprehensive, well-structured notes from the following content. Use bold and larger font sizes for headings, and break down each section into bullet points with either dots or numbered lists. Ensure that the content is detailed and includes explanations of key concepts, examples, and any relevant information, making it easy to understand for someone new to the topic:

    {translated_text}
    """

processed_content = process_content(prompt, user_preference)
print(f"Processed Content: {processed_content}")

summarize = input("Would you like to summarize the content? (yes/no): ")
if summarize.lower() == 'yes':
    summary = summarize_content(processed_content)
    print(f"Summary: {summary}")
else:
    summary = processed_content

# Generating a title using OpenAI based on the content
title_prompt = f"Generate a concise and relevant title for the following notes:\n\n{
    summary}"
title_response = openai.Completion.create(
    engine="gpt-3.5-turbo-instruct",
    prompt=title_prompt,
    max_tokens=50
)
title = title_response.choices[0].text.strip()

generate_pdf(None, summary, title, processed_content)
print(f"PDF generated: {title.replace(' ', '_')}_Notes.pdf")
