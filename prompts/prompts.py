from utils.config import TONE, CHAPTER_LIMIT


def planner_prompt(brief):
    return f"""
You are a professional book planner.

Return ONLY valid JSON. No explanation.

Structure:
{{
  "title": "Book Title",
  "chapters": [
    {{
      "title": "Chapter Title",
      "summary": "Short summary"
    }}
  ]
}}

STRICT RULES:
- Generate EXACTLY {CHAPTER_LIMIT} chapters
- Each chapter must be unique
- Tone: {TONE}

Topic:
{brief}
"""