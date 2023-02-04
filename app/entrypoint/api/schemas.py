from pydantic import BaseModel, constr
from datetime import datetime


class Customer(BaseModel):
    document: constr(regex=r"^([0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2})$")
    name: str

class Product(BaseModel):
    type: str
    value: float
    qty: int

class Sale(BaseModel):
    sold_at: datetime
    customer: Customer
    total: float
    products: list[Product]
