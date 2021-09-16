import uvicorn

from api.app import create_app
from api.config import ProductionConfig

application = create_app(config_object=ProductionConfig)

if __name__ == "__main__":
    uvicorn.run(application, host="0.0.0.0", port=5000)
