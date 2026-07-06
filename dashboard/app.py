import os
import random
from flask import Flask, render_template, redirect, url_for, flash
from dotenv import load_dotenv

# Allow dashboard to use same bot config
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"), override=False)

import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src import telegram_client as tg
from src import pollinations_client as ai
from src.templates import TEXT_TEMPLATES, TOPICS
from src.main import LANGUAGES

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret-key")


@app.route("/")
def index():
    return render_template("dashboard.html", languages=LANGUAGES, topics=TOPICS)


@app.route("/send/daily-pair")
def send_daily_pair():
    topic = random.choice(TOPICS)
    selected_langs = random.sample(LANGUAGES, 2)
    
    for lang in selected_langs:
        try:
            prompt_func = TEXT_TEMPLATES["language_prompt"]
            prompt = prompt_func(lang, topic)
            text_content = ai.generate_text(prompt)
            tg.send_text(text_content)
        except Exception as e:
            flash(f"Error posting for {lang}: {e}", "error")
            
    flash(f"Daily pair sent successfully for {', '.join(selected_langs)} (Topic: {topic})!", "success")
    return redirect(url_for("index"))


@app.route("/send/language/<lang>")
def send_language_card(lang):
    if lang not in LANGUAGES:
        flash("Invalid language selected.", "error")
        return redirect(url_for("index"))
        
    topic = random.choice(TOPICS)
    try:
        prompt_func = TEXT_TEMPLATES["language_prompt"]
        prompt = prompt_func(lang, topic)
        text_content = ai.generate_text(prompt)
        tg.send_text(text_content)
        flash(f"Manually sent {lang} vocabulary card (Topic: {topic})!", "success")
    except Exception as e:
        flash(f"Error posting for {lang}: {e}", "error")
        
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
