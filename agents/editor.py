from utils.groq_client import generate


def edit(text):
    prompt = f"""
Edit this text for clarity and flow.

- Fix awkward phrasing
- Improve readability
- Keep tone consistent

Text:
{text}
"""
    return generate(prompt)