from fastapi import FastAPI

from api import __version__ as api_version
from api import controller
from api.config import get_logger, settings

_logger = get_logger(logger_name=__name__)


app = FastAPI(title=settings.PROJECT_NAME, version=api_version)
app.include_router(controller.router)


@app.get("/health")
async def health():
    _logger.info("health status OK")
    return "ok"


_logger.debug("Application instance created")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="debug")
