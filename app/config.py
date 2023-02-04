from pydantic import BaseSettings


class Settings(BaseSettings):
    jwt_secret_key: str = "erp-wallet"

    class Config:
        env_file = ".env"
        env_file_encondig =  "utf-8"


def make_settings() -> Settings:
    return Settings()
