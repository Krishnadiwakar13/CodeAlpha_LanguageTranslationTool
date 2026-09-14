import os

import deepl
from dotenv import load_dotenv


load_dotenv()

DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")

if not DEEPL_API_KEY:
    raise ValueError("DEEPL_API_KEY is not set in the .env file")


translator = deepl.DeepLClient(DEEPL_API_KEY)


TARGET_LANGUAGE_MAP = {
    "en": "EN-US",
    "pt": "PT-PT",
    "zh": "ZH-HANS",
}


def translate_text(text, source_language, target_language):
    """
    Translate text using the DeepL API.
    """

    if not text.strip():
        return ""

    if source_language.lower() == target_language.lower():
        return text

    target_language = TARGET_LANGUAGE_MAP.get(
        target_language.lower(),
        target_language.upper(),
    )

    source_language = source_language.upper()

    result = translator.translate_text(
        text,
        source_lang=source_language,
        target_lang=target_language,
    )

    return result.tex