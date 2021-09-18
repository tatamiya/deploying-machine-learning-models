from typing import List

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from regression_model import __version__ as _version
from regression_model.predict import make_prediction

from api import __version__ as api_version
from api.config import get_logger
from api.schema import HouseData, PredictionResults, Version

router = APIRouter(prefix="")

_logger = get_logger(logger_name=__name__)


@router.get("/health")
async def health():
    _logger.info("health status OK")
    return "ok"


@router.get("/version", response_model=Version)
async def version():
    return {"model_version": _version, "api_version": api_version}


@router.post("/v1/predict/regression", response_model=PredictionResults)
async def predict(data: List[HouseData]):

    _logger.debug(f"Inputs: {data}")

    # Step 3: Model prediction
    result = make_prediction(input_data=jsonable_encoder(data))
    _logger.debug(f"Outputs: {result}")

    # Step 4: Convert numpy array to list
    predictions = result.get("predictions").tolist()
    version = result.get("version")

    # Step 5: Return the response as JSON
    return {"predictions": predictions, "version": version}
