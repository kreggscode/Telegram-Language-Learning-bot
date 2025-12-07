
def get_language_prompt(language: str) -> str:
    """
    Generates a prompt for a specific language.
    """
    base_prompt = f"""
Generate a list of 10 useful, everyday phrases in {language} for a beginner language learner.
For each phrase, provide:
1. The phrase in the native script.
2. The Romanization/Pinyin (ONLY for non-Latin scripts like Russian, Chinese, Korean, Japanese, Hebrew). Format this line in italics (surrounded by underscores, e.g. _ni hao_). DO NOT write the word "Romanization" or "Pinyin" before it. Just the text.
3. The English translation.

Format neatly as a list.
Ensure the phrases are distinct, practical, and not repeats of generic "Hello/Goodbye". 
Add a small "Cultural Note" or "Grammar Tip" at the end specific to these phrases.

IMPORTANT:
- For {language}, if it uses a non-Latin script, YOU MUST INCLUDE THE ROMANIZATION in italics on the line below the native phrase.
- Do not number them simply 1-10, use emojis like 🔸.
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
