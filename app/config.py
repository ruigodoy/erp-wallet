from pydantic import BaseSettings

class Settings(BaseSettings):
    jwt_secret_key: str = "erp-wallet"
    url_db: str = "postgresql://erp_user:erp_pass@localhost:5432/erpwallet"

    class Config:
        env_file = ".env"
        env_file_encondig =  "utf-8"


def make_settings() -> Settings:
    return Settings()
