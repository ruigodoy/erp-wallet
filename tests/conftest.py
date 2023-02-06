import pytest
from jose import jwt
from fastapi.testclient import TestClient
from app.entrypoint.api import main


@pytest.fixture
def client_http() -> TestClient:
    return TestClient(main.app)


@pytest.fixture
def jwt_token():
    payload = {
        "name": "User Test",
        "permission": "full-access"
    }
    token = jwt.encode(payload, "erp-wallet", algorithm="HS256")
    return token