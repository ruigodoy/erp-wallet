from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import JSON

Base = declarative_base()

class Sale(Base):
    __tablename__ = "sale"

    id = Column(Integer, primary_key=True)
    sold_at = Column(Date)
    document = Column(String)
    name = Column(String)
    total = Column(Float)
    products = Column(JSON)


class CashBack(Base):
    __tablename__ = "cashback"

    id = Column(Integer, primary_key=True)
    created_at = Column(Date)
    message = Column(String)
    document = Column(String)
    cashback = Column(Float)
