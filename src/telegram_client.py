import requests
from .config import BOT_TOKEN, CHAT_ID

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def send_text(text: str):
    url = f"{BASE_URL}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    resp = requests.post(url, data=data)
    if resp.status_code != 200:
        print(f"FAILED to send message to Telegram. Status: {resp.status_code}")
        print(f"Response: {resp.text}")
        # Try fallback without markdown
        if "Bad Request: can't parse entities" in resp.text:
            print("Retrying without Markdown...")
            data_no_md = data.copy()
            data_no_md.pop("parse_mode", None)
            resp_retry = requests.post(url, data=data_no_md)
            if resp_retry.status_code == 200:
                print("Retry successful (without Markdown).")
                return resp_retry
            else:
                print(f"Retry also FAILED. Status: {resp_retry.status_code}")
                print(f"Retry Response: {resp_retry.text}")
                return resp_retry
    else:
        print(f"Successfully sent message to Telegram (Chat: {CHAT_ID}).")
    return resp


def send_photo(image_url: str, caption: str = ""):
    url = f"{BASE_URL}/sendPhoto"
    data = {
        "chat_id": CHAT_ID,
        "photo": image_url,
        "caption": caption,
        "parse_mode": "Markdown"
    }
    resp = requests.post(url, data=data)
    return resp


def send_poll(question: str, options: list[str]):
    import json
    url = f"{BASE_URL}/sendPoll"
    data = {
        "chat_id": CHAT_ID,
        "question": question,
        "options": json.dumps(options),
        "is_anonymous": False
    }
    resp = requests.post(url, data=data)
    return resp


def send_thread(messages: list[str]):
    for msg in messages:
        send_text(msg)
