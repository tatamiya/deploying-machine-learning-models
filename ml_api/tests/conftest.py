import pytest
from api.app import create_app
from fastapi.testclient import TestClient


@pytest.fixture
def app():
    return create_app()


@pytest.fixture
def test_client(app):
    return TestClient(app)
