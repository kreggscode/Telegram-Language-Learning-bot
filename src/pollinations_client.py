import urllib.parse
import requests
import random
from .config import POLLINATIONS_API_KEY, AI_MODEL

def generate_text(prompt: str, max_retries: int = 3) -> str:
    """Generate text from Pollinations.ai using ONLY the paid API endpoint with retry logic."""
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
    
    import time
    for attempt in range(max_retries):
        try:
            print(f"Calling Pollinations API (Attempt {attempt + 1}/{max_retries})...")
            resp = requests.post("https://gen.pollinations.ai/v1/chat/completions", json=payload, headers=headers, timeout=40)
            if resp.status_code == 200:
                data = resp.json()
                return data["choices"][0]["message"]["content"].strip()
            elif resp.status_code == 429:
                print(f"Rate limited (429). Retrying after sleep...")
                time.sleep(5 * (attempt + 1))
            else:
                print(f"API Error {resp.status_code}: {resp.text}")
                time.sleep(2)
        except Exception as e:
            print(f"Attempt {attempt + 1} failed with exception: {e}")
            time.sleep(2)
            
    return "⚠️ AI generation failed after multiple attempts due to API timeouts or errors."


def image_url(prompt: str) -> str:
    """Return an image URL from Pollinations using ONLY the paid API endpoint."""
    if not POLLINATIONS_API_KEY:
        raise RuntimeError("FATAL: POLLINATIONS_API_KEY is missing. Paid API usage is REQUIRED.")

    seed = random.randint(1000, 999999)
    encoded = urllib.parse.quote(prompt)
    
    # Using ONLY the paid gateway with the API key
    return f"https://gen.pollinations.ai/image/{encoded}?model=flux&seed={seed}&key={POLLINATIONS_API_KEY}"
