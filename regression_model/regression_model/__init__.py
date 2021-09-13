import logging
from importlib import metadata

from regression_model.config import logging_config

# Configure logger for use in package
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging_config.get_console_handler())
logger.propagate = False


__version__ = metadata.version("regression_model")
