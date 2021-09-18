import pytest
from fastapi.testclient import TestClient

from api.app import create_app
from api.config import TestingConfig


@pytest.fixture
def app():
    return create_app(config_object=TestingConfig)


@pytest.fixture
def test_client(app):
    return TestClient(app)
