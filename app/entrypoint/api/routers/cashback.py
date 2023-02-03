import json

from fastapi import APIRouter, Depends, Body
from app.entrypoint.api import dependencies

router = APIRouter(
    dependencies=[
        Depends(dependencies.auth_required),
    ]
)


@router.post("/api/cashback")
def send_cashback(body: dict = Body(...)):
    return body