import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from datetime import datetime
from from_root import from_root


def setup_logger():

    log_dir = os.path.join(from_root(), "logs")
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(
        log_dir,
        f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
    )

    logger = logging.getLogger("us_visa")
    logger.setLevel(logging.INFO)

    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter(
        "[%(asctime)s] %(name)s - %(levelname)s - %(message)s"
    )

    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=5 * 1024 * 1024,
        backupCount=3
    )

    console_handler = logging.StreamHandler(sys.stdout)

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger