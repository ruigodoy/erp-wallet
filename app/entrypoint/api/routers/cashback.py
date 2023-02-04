from fastapi import APIRouter, Depends, HTTPException, status
from app.entrypoint.api import dependencies, schemas
from app.entrypoint.repositories import PostgresRepository
from app.entrypoint.utils import mapper_schema_to_model_sale, mapper_dict_to_model_cashback
from app.entrypoint.factories import get_client
from requests.exceptions import HTTPError

router = APIRouter(
    dependencies=[
        Depends(dependencies.auth_required),
    ]
)


@router.post("/api/cashback")
def cashback(
    sale: schemas.Sale,
    postgres_repository: PostgresRepository = Depends(
        dependencies.make_postgres_repository,
    )
) -> schemas.Sale:
    invalidate_sum_total = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="The sum of the products does not equal the total!",
    )
    try:
        _validate_sum_total(sale=sale)
        postgres_repository.insert_row(mapper_schema_to_model_sale(sale))
        _send_cashback_request(sale, postgres_repository)
    except ValueError:
        raise invalidate_sum_total
    except HTTPError as e:
        external_api_error = HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
        raise external_api_error
    return sale


def _validate_sum_total(sale: schemas.Sale):
    total = sale.total
    sum_total_products = 0
    
    for product in sale.products:
        sum_total_products += product.value
    
    if total != sum_total_products:
        raise ValueError
    return True


def _send_cashback_request(
    sale: schemas.Sale, 
    postgres_repository: PostgresRepository
) -> None:
    client = get_client()

    data = {
        "document": sale.customer.document,
        "cashback": _calculate_cashback(sale)
    }

    response = client.make_cashback(data)
    postgres_repository.insert_row(mapper_dict_to_model_cashback(response))


def _calculate_cashback(sale: schemas.Sale) -> int:
    products = sale.products
    total = sale.total
    cashback = 0

    if len(products) > 2:
        cashback = total - (total * 0.1)
    elif len(products) > 3:
        cashback = total - (total * 0.2)
    elif len(products) > 4:
        cashback = total - (total * 0.3)
    else:
        cashback = total - (total * 0.4)

    return cashback
