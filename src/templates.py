
def get_language_prompt(language: str) -> str:
    """
    Generates a prompt for a specific language.
    """
    base_prompt = f"""
Generate a list of 10 useful, everyday phrases in {language} for a beginner language learner.
For each phrase, provide:
1. The phrase in the native script (if applicable).
2. The Romanization/Pinyin (CRITICAL for Russian, Chinese, Korean, Japanese, Hebrew, etc.).
3. The English translation.

Format neatly as a list.
Ensure the phrases are distinct, practical, and not repeats of generic "Hello/Goodbye". 
Add a small "Cultural Note" or "Grammar Tip" at the end specific to these phrases.

IMPORTANT:
- If {language} uses a non-Latin script (like Russian, Chinese, Korean, Japanese, Hebrew), YOU MUST INCLUDE THE ROMANIZATION/TRANSLITERATION.
- Do not number them simply 1-10, make them formatted for a Telegram message (maybe use emojis like 🔸).
- Add a header line: "🌍 Learning {language}: Daily Phrases 🌍"
"""
    return base_prompt

TEXT_TEMPLATES = {
    "language_prompt": get_language_prompt
}

IMAGE_TEMPLATES = {
    # Keep some generic ones or language specific if we want images later
    "default": "A beautiful, minimalist educational illustration about language learning, vector art style, flat design, soft colors"
}
