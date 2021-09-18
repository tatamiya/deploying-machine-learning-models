from fastapi import FastAPI

from api import __version__ as api_version
from api.config import get_logger, settings

_logger = get_logger(logger_name=__name__)


def create_app() -> FastAPI:
    """Create a FastAPI app instance."""

    app = FastAPI(title=settings.PROJECT_NAME, version=api_version)

    # import blueprints
    from api import controller

    app.include_router(controller.router)

    _logger.debug("Application instance created")

    return app
