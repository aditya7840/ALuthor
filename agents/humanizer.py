from utils.groq_client import generate
from utils.config import TONE


def humanize(text):
    prompt = f"""
Rewrite this text in a {TONE} tone.

Rules:
- Remove AI-like phrases
- Vary sentence length
- Make it sound human
- Keep meaning same

Text:
{text}
"""
    return generate(prompt)