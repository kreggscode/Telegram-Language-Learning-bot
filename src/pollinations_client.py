import urllib.parse
import requests
import random
from .config import POLLINATIONS_API_KEY, AI_MODEL

def generate_text(prompt: str) -> str:
    """Generate text from Pollinations.ai using ONLY the paid API endpoint."""
    if not POLLINATIONS_API_KEY:
        raise RuntimeError("FATAL: POLLINATIONS_API_KEY is missing. Paid API usage is REQUIRED.")

    headers = {
        "Authorization": f"Bearer {POLLINATIONS_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Add randomization to ensure unique content
    seed = random.randint(1000, 999999)
    enhanced_prompt = f"{prompt}\n\n(Random seed: {seed})"
    
    payload = {
        "model": AI_MODEL,
        "messages": [{"role": "user", "content": enhanced_prompt}],
        "seed": seed
    }
    
    try:
        resp = requests.post("https://gen.pollinations.ai/v1/chat/completions", json=payload, headers=headers, timeout=60)
        if resp.status_code == 200:
            data = resp.json()
            return data["choices"][0]["message"]["content"].strip()
        else:
            err_msg = f"Paid API Error: {resp.status_code} - {resp.text}"
            print(err_msg)
            return f"⚠️ AI generation failed (Paid API Status {resp.status_code})."
    except Exception as e:
        print(f"Request Exception: {e}")
        return "⚠️ AI generation failed due to a connection error with the paid API."


def image_url(prompt: str) -> str:
    """Return an image URL from Pollinations using ONLY the paid API endpoint."""
    if not POLLINATIONS_API_KEY:
        raise RuntimeError("FATAL: POLLINATIONS_API_KEY is missing. Paid API usage is REQUIRED.")

    seed = random.randint(1000, 999999)
    encoded = urllib.parse.quote(prompt)
    
    # Using ONLY the paid gateway with the API key
    return f"https://gen.pollinations.ai/image/{encoded}?model=flux&seed={seed}&key={POLLINATIONS_API_KEY}"
