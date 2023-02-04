from app.entrypoint import models
from app.entrypoint.api import schemas
import json


def mapper(cashback_schema: schemas.CashBack) -> models.CashBack:
    cashback_dict = cashback_schema.dict()
    products_json = json.dumps(cashback_dict["products"])

    cashback = models.CashBack(
        sold_at=cashback_schema.sold_at,
        document=cashback_schema.customer.document,
        name=cashback_schema.customer.name,
        total=cashback_schema.total,
        products=products_json
    )

    return cashback