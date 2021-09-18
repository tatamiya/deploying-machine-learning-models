import pytest
from api.app import app
from fastapi.testclient import TestClient


@pytest.fixture
def test_client():
    return TestClient(app)
