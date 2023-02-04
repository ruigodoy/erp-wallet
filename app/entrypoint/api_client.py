import requests
from typing import Any

class Client:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers = {
            "Content-Type": "application/json",
        }
    
    def make_cashback(self, data) -> dict[str, Any]:
        endpoint = "/api/mock/Cashback"
        url = self.base_url + endpoint

        result = self.session.post(url, json=data)
        result.raise_for_status()

        return result.json()