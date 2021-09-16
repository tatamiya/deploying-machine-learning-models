import pytest
from api.app import create_app
from api.config import TestingConfig
from fastapi.testclient import TestClient


@pytest.fixture
def app():
    return create_app(config_object=TestingConfig)


@pytest.fixture
def test_client(app):
    return TestClient(app)
