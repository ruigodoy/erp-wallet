from sqlalchemy import create_engine
from app.entrypoint.models import Base
from app import config

settings = config.make_settings()

engine = create_engine(settings.url_db)


def create_database():
    Base.metadata.create_all(engine)


def drop_database():
    Base.metadata.drop_all(engine)
