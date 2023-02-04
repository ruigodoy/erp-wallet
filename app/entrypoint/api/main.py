from fastapi import FastAPI
from .routers import cashback

from app.entrypoint.database import create_database, drop_database

app = FastAPI(
    title="ERP Wallet API",
    version="1.0.0",
)

app.include_router(cashback.router)


@app.on_event("startup")
async def startup_event() -> None:
    create_database()


@app.on_event("shutdown")
async def shutdown_event() -> None:
    drop_database()
