from fastapi.testclient import TestClient
from tests.data import *

def test_cashback(
    client_http: TestClient,
    jwt_token: str,
):
    headers = {
        "Authorization": jwt_token
    }
    
    response = client_http.post("/api/cashback", json=CASH_BACK_PAYLOAD, headers=headers)
    assert response.status_code == 200


def test_cashback_with_invalid_date(
    client_http: TestClient,
    jwt_token: str,
):
    headers = {
        "Authorization": jwt_token
    }
    
    response = client_http.post(
        "/api/cashback", 
        json=CASH_BACK_PAYLOAD_WITH_INVALID_DATE, 
        headers=headers
    )
    assert response.status_code == 422


def test_cashback_with_invalid_document(
    client_http: TestClient,
    jwt_token: str,
):
    headers = {
        "Authorization": jwt_token
    }
    
    response = client_http.post(
        "/api/cashback", 
        json=CASH_BACK_PAYLOAD_WITH_DOCUMENT, 
        headers=headers
    )
    assert response.status_code == 422


def test_cashback_with_invalid_total(
    client_http: TestClient,
    jwt_token: str,
):
    headers = {
        "Authorization": jwt_token
    }
    
    response = client_http.post(
        "/api/cashback", 
        json=CASH_BACK_PAYLOAD_WITH_TOTAL, 
        headers=headers
    )
    assert response.status_code == 400
