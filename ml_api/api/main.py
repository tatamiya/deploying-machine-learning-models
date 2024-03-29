from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import __version__ as api_version
from api import predict
from api.config import get_logger, settings

_logger = get_logger(logger_name=__name__)


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=api_version,
    openapi_url=f"{settings.VERSIONED_PREFIX}/openapi.json",
)
app.include_router(predict.router)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.get("/health")
async def health():
    _logger.info("health status OK")
    return "ok"


_logger.debug("Application instance created")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="debug")
