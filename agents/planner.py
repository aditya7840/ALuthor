import json
from utils.groq_client import generate
from prompts.prompts import planner_prompt
from utils.config import CHAPTER_LIMIT
from utils.loggers import get_logger

logger = get_logger("planner")


def safe_plan(brief, retries=3):
    for attempt in range(retries):
        logger.info(f"Planner attempt {attempt+1}")

        raw = generate(planner_prompt(brief))

        try:
            start = raw.find("{")
            end = raw.rfind("}") + 1
            data = json.loads(raw[start:end])

            chapters = data.get("chapters", [])

            if len(chapters) < CHAPTER_LIMIT:
                logger.warning("Not enough chapters, retrying...")
                continue

            data["chapters"] = chapters[:CHAPTER_LIMIT]

            return data

        except Exception as e:
            logger.error("Planner failed", exc_info=True)

    raise Exception("Planner failed after retries")