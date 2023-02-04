from app.entrypoint import models
from app.entrypoint.api import schemas
from typing import Any
import json


def mapper_schema_to_model_sale(sale_schema: schemas.Sale) -> models.Sale:
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

def mapper_dict_to_model_cashback(cashback: dict[str, Any]) -> models.CashBack:
    cashback = models.CashBack(
        id=cashback["id"],
        created_at=cashback["createdAt"],
        message=cashback["message"],
        documnet=cashback["document"],
        cashback=cashback["cashback"]
    )
    return cashback
