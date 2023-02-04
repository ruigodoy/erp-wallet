from app.entrypoint.database import engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

class PostgresRepository:
    def insert_row(self, data) -> None:
        session = Session()
        
        session.add(data)
        session.commit()

        session.close()
