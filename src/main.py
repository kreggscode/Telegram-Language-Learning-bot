from . import pollinations_client as ai
from . import telegram_client as tg
from . import scheduler_logic as sched
from .templates import TEXT_TEMPLATES
import random
import time

# List of languages as defined by user requirements
LANGUAGES = [
    "German",
    "Spanish",
    "Russian",
    "Chinese (Mandarin)",
    "Korean",
    "Italian",
    "Japanese",
    "Hebrew"
]

def post_language_pair():
    """
    Selects 2 distinct languages and posts a learning card for each.
    """
    # Select 2 unique languages
    selected_langs = random.sample(LANGUAGES, 2)
    
    print(f"Selected languages for this run: {selected_langs}")

    for lang in selected_langs:
        try:
            # Generate content
            prompt_func = TEXT_TEMPLATES["language_prompt"]
            prompt = prompt_func(lang)
            
            print(f"Generating content for {lang}...")
            text_content = ai.generate_text(prompt)
            
            # Send to Telegram
            tg.send_text(text_content)
            
            # Small delay to prevent rate limits or message ordering issues
            time.sleep(2)
            
        except Exception as e:
            print(f"Error posting for {lang}: {e}")
            tg.send_text(f"⚠️ Error generating content for {lang}. Please check logs.")
    
    print("Post language pair run completed.")


def main():
    post_type = sched.decide_post_type()
    print(f"Decided post type: {post_type}")

    if post_type == "language_pair":
        post_language_pair()
    else:
        tg.send_text("No valid post type decided.")


if __name__ == "__main__":
    main()
