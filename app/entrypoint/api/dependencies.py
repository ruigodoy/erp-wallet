from fastapi import Depends, HTTPException, Security, status
from fastapi.security import APIKeyHeader
from jose import jwt, JWTError
from app import config
from app.entrypoint.repositories import PostgresRepository 

API_KEY_HEADER = APIKeyHeader(name="Authorization", auto_error=True)


def auth_required(
    settings: config.Settings = Depends(config.make_settings),
    key: str = Security(API_KEY_HEADER)
):
    invalidate_auth_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate the credentials!",
        headers={"Authenticate": "Bearer"}
    )
    try:
        jwt_payload = jwt.decode(key, settings.jwt_secret_key, algorithms=["HS256"])
        permission = jwt_payload.get("permission")

        if permission is None or permission != "full-access":
            raise invalidate_auth_exception
    except JWTError:
        raise invalidate_auth_exception


def make_postgres_repository() -> PostgresRepository:
    return PostgresRepository()
