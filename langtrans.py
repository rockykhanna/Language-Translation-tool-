import googletrans
from googletrans import Translator

def translate_text(text, source_language, target_language):
    """Translates the given text from the source language to the target language."""
    translator = Translator()
    translated_text = translator.translate(text, src=source_language, dest=target_language)
    return translated_text.text

# Get user input
source_text = input("Enter the text to be translated: ")
source_language = input("Enter the source language code (e.g., en for English): ")
target_language = input("Enter the target language code (e.g., fr for French): ")

# Translate the text
translated_text = translate_text(source_text, source_language, target_language)

# Print the translated text
print("Translated text:")
print(translated_text)