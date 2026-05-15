from agents.planner import safe_plan
from agents.writer import write_chapter
from agents.humanizer import humanize
from agents.editor import edit
from memory.memory import init_memory
from assembler.assembler import assemble_book
from utils.formatter import create_pdf
from utils.config import TONE
from utils.loggers import setup_logger, get_logger


def run(brief):
    setup_logger()
    logger = get_logger("orchestrator")

    logger.info("Starting pipeline")

    try:
        init_memory(TONE)

        outline = safe_plan(brief)
        title = outline["title"]
        chapters = outline["chapters"]

        full_chapters = []

        for ch in chapters:
            content = write_chapter(ch, brief)
            content = humanize(content)
            content = edit(content)

            full_chapters.append({
                "title": ch["title"],
                "content": content
            })

        book = assemble_book(title, full_chapters)

        create_pdf(book)

        logger.info("Pipeline completed successfully")

    except Exception as e:
        logger.error("Pipeline failed", exc_info=True)


if __name__ == "__main__":
    run("Beginner guide to personal finance")