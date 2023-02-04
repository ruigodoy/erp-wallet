from app.entrypoint import models
from app.entrypoint.api import schemas
import json


def mapper(sale_schema: schemas.Sale) -> models.CashBack:
    sale_dict = sale_schema.dict()
    products_json = json.dumps(sale_dict["products"])

    sale = models.Sale(
        sold_at=sale_schema.sold_at,
        document=sale_schema.customer.document,
        name=sale_schema.customer.name,
        total=sale_schema.total,
        products=products_json
    )

    return sale