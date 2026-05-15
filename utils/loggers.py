import logging
import os


def setup_logger():
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        filename="logs/app.log",
        level=logging.INFO,
        format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    )


def get_logger(name):
    return logging.getLogger(name)