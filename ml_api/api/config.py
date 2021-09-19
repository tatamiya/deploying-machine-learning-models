import logging
import pathlib
import sys
from logging.handlers import TimedRotatingFileHandler
from typing import List

from pydantic import AnyHttpUrl, BaseSettings

PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent.parent

FORMATTER = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s -" "%(funcName)s:%(lineno)d - %(message)s"
)
LOG_DIR = PACKAGE_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "ml_api.log"


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler():
    file_handler = TimedRotatingFileHandler(LOG_FILE, when="midnight")
    file_handler.setFormatter(FORMATTER)
    file_handler.setLevel(logging.WARNING)
    return file_handler


def get_logger(*, logger_name):
    """Get logger with prepared handlers."""

    logger = logging.getLogger(logger_name)

    logger.setLevel(logging.INFO)

    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    logger.propagate = False

    return logger


class APISettings(BaseSettings):
    PROJECT_NAME: str = "House Price Prediction API"
    VERSIONED_PREFIX: str = "/v1"

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:5000",  # type: ignore
        "https://localhost:5000",  # type: ignore
    ]


settings = APISettings()
