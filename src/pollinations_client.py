import urllib.parse
import requests
import random
import time
from datetime import datetime
from .config import POLLINATIONS_API_KEY, AI_MODEL


def generate_text(prompt: str) -> str:
    """Generate text from Pollinations.ai using the paid API endpoint."""
    if not POLLINATIONS_API_KEY:
        # Fallback to free endpoint if key is missing, though user wants paid
        seed = random.randint(1000, 999999)
        encoded = urllib.parse.quote(prompt)
        url = f"https://text.pollinations.ai/{encoded}?seed={seed}"
        resp = requests.get(url, timeout=30)
        return resp.text.strip() if resp.status_code == 200 else "AI generation failed. Please try again."

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
            print(f"API Error: {resp.status_code} - {resp.text}")
            return f"AI generation failed (Status {resp.status_code}). Please try again."
    except Exception as e:
        print(f"Request Exception: {e}")
        return "AI generation failed due to a connection error."


def image_url(prompt: str) -> str:
    """Return an image URL from Pollinations based on prompt with specialization for paid API."""
    seed = random.randint(1000, 999999)
    encoded = urllib.parse.quote(prompt)
    
    if POLLINATIONS_API_KEY:
        # Using the paid gateway with the API key
        return f"https://gen.pollinations.ai/image/{encoded}?model=flux&seed={seed}&key={POLLINATIONS_API_KEY}"
    
    # Fallback to free endpoint
    return f"https://image.pollinations.ai/prompt/{encoded}?seed={seed}"
