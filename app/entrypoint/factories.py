from app import config
from app.entrypoint.api_client import Client

settings = config.make_settings()
_client: Client = None


def get_client():
    global _client

    if _client:
        return _client
    
    _client = Client(base_url=settings.base_api_url)
    return _client
