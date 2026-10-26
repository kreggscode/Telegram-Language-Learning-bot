
TOPICS = [
    "Greetings & Basic Introductions",
    "At a Restaurant: Ordering Food & Drinks",
    "Directions, Transportation & Navigation",
    "Shopping: Clothes, Souvenirs & Prices",
    "Emergency Situations & Requesting Help",
    "Telling Time, Days, Months & Seasons",
    "Talking About Family & Friends",
    "Hobbies, Leisure Activities & Sports",
    "Hotel Check-in & Accommodation",
    "Expressing Emotions, Feelings & Opinions",
    "Numbers, Counting & Money",
    "Useful Classroom & Learning Phrases (e.g., 'Repeat please', 'I don't understand')",
    "Weather, Temperature & Climate",
    "At the Airport & Travel Documents",
    "Describing Daily Routines & Activities",
    "Talking About Occupations, Work & School",
    "In a City: Sightseeing & Tourism",
    "At the Market: Fresh Produce & Food Items",
    "Common Adjectives (Describing Size, Quality, Color)",
    "Conversational Fillers & Casual Chatting"
]

def get_language_prompt(language: str, topic: str) -> str:
    """
    Generates a prompt for a specific language and topic.
    """
    base_prompt = f"""
🌍 Learning {language}: Daily Phrases 🌍
📚 Topic: {topic}

Generate a list of 10 useful, everyday phrases in {language} for a beginner language learner specifically related to the topic "{topic}".
For each phrase, provide:
1. The phrase in the native script.
2. The Romanization/Pinyin (ONLY for non-Latin scripts like Russian, Chinese, Korean, Japanese, Hebrew). Format this line in italics (surrounded by underscores, e.g. _ni hao_). DO NOT write the word "Romanization" or "Pinyin" or any label before it. Just the italicized text.
3. The English translation.

Format neatly as a list.
Ensure the phrases are distinct, practical, and highly relevant to the topic "{topic}". 
Add a small "Cultural Note" or "Grammar Tip" at the end specific to these phrases or this topic.

IMPORTANT:
- For {language}, if it uses a non-Latin script, YOU MUST INCLUDE THE ROMANIZATION in italics on the line below the native phrase.
- Do not number them simply 1-10, use emojis like 🔸.
- Add a header line at the very top: "🌍 Learning {language}: Daily Phrases 🌍"
- On the second line, state the topic: "📚 Topic: {topic}"
"""
    return base_prompt

TEXT_TEMPLATES = {
    "language_prompt": get_language_prompt
}

IMAGE_TEMPLATES = {
    "default": "A beautiful, minimalist educational illustration about language learning, vector art style, flat design, soft colors"
}

HASHTAGS = {
    "German": "\n\n🔍 **Topics:** German Vocabulary • Daily Deutsch • German Phrases • Goethe A1-B2\n#German #LearnGerman #LanguageLearning #Deutsch #DailyGerman #Polyglot #GermanGrammar",
    "Spanish": "\n\n🔍 **Topics:** Spanish Phrases • Español Vocabulario • Conversational Spanish • DELE\n#Spanish #LearnSpanish #LanguageLearning #Español #DailySpanish #Polyglot #LearnSpanishDaily",
    "Russian": "\n\n🔍 **Topics:** Russian Phrases • Cyrillic Pronunciation • Daily Russian • TORFL\n#Russian #LearnRussian #LanguageLearning #Русский #DailyRussian #Polyglot #RussianGrammar",
    "Chinese (Mandarin)": "\n\n🔍 **Topics:** Mandarin Chinese • Pinyin & Characters • HSK Vocabulary • Spoken Chinese\n#Chinese #Mandarin #LearnChinese #LanguageLearning #DailyChinese #HSK #Zhongwen",
    "Korean": "\n\n🔍 **Topics:** Korean Hangul • Daily Korean Expressions • TOPIK Vocab • K-Culture\n#Korean #LearnKorean #LanguageLearning #한국어 #DailyKorean #TOPIK #Hangul",
    "Italian": "\n\n🔍 **Topics:** Italian Expressions • Italiano Vocabolario • Italian Grammar • Travel Italy\n#Italian #LearnItalian #LanguageLearning #Italiano #DailyItalian #Polyglot #LearnItalian",
    "Japanese": "\n\n🔍 **Topics:** Japanese Kanji • Hiragana/Katakana • JLPT N5-N1 • Daily Nihongo\n#Japanese #LearnJapanese #LanguageLearning #日本語 #DailyJapanese #JLPT #Nihongo",
    "Hebrew": "\n\n🔍 **Topics:** Hebrew Alphabet • Modern Ivrit • Daily Hebrew • Ulpan Vocab\n#Hebrew #LearnHebrew #LanguageLearning #עברית #DailyHebrew #Polyglot #Ivrit"
}
