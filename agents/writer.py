from utils.groq_client import generate
from memory.memory import get_memory
from rag.rag import retrieve
from utils.loggers import get_logger

logger = get_logger("writer")


def write_chapter(chapter, topic):
    logger.info(f"Writing chapter: {chapter['title']}")

    mem = get_memory()
    rag_data = retrieve(topic)

    prompt = f"""
Write a detailed book chapter.

Title: {chapter['title']}
Summary: {chapter['summary']}

Tone: {mem['tone']}

Use these facts:
{rag_data}

Make it natural and readable.
"""

    return generate(prompt)