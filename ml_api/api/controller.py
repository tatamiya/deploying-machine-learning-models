from fastapi import APIRouter, Request
from regression_model import __version__ as _version
from regression_model.predict import make_prediction

from api import __version__ as api_version
from api.config import get_logger
from api.validation import validate_inputs

router = APIRouter(prefix="")

_logger = get_logger(logger_name=__name__)


@router.get("/health")
async def health():
    _logger.info("health status OK")
    return "ok"


@router.get("/version")
async def version():
    return {"model_version": _version, "api_version": api_version}


@router.post("/v1/predict/regression")
async def predict(request: Request):
    # Step 1: Extract POST dtaa from request body as JSON
    json_data = await request.json()
    _logger.debug(f"Inputs: {json_data}")

    # Step 2: Validate the input using marshmallow schema
    input_data, errors = validate_inputs(input_data=json_data)

    # Step 3: Model prediction
    result = make_prediction(input_data=input_data)
    _logger.debug(f"Outputs: {result}")

    # Step 4: Convert numpy array to list
    predictions = result.get("predictions").tolist()
    version = result.get("version")

    # Step 5: Return the response as JSON
    return {"predictions": predictions, "version": version, "errors": errors}
