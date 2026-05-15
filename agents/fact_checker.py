from utils.groq_client import generate


def fact_check(text):
    prompt = f"""
Check this text for factual issues.

If something seems incorrect:
- Correct it
- Or soften the claim

Text:
{text}
"""
    return generate(prompt)