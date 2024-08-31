from langdetect import detect
import openai


def translate_text_if_needed(text, target_language="English"):
    # Detect the language of the text
    detected_language = detect(text)

    # If the text is already in English, return it as is
    if detected_language.lower() == "en":
        return text

    # Otherwise, translate it to English
    prompt = f"Translate the following text to {target_language}: {text}"
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=1024
    )
    return response.choices[0].text.strip()
