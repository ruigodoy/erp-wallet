from fastapi import APIRouter, Depends, HTTPException, status
from app.entrypoint.api import dependencies, schemas
from app.entrypoint.repositories import PostgresRepository
from app.entrypoint.utils import mapper

router = APIRouter(
    dependencies=[
        Depends(dependencies.auth_required),
    ]
)


@router.post("/api/cashback")
def cashback(
    cashback: schemas.CashBack,
    postgres_repository: PostgresRepository = Depends(
        dependencies.make_postgres_repository,
    )
) -> schemas.CashBack:
    invalidate_sum_total = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="The sum of the products does not equal the total!",
    )
    try:
        _validate_sum_total(cashback=cashback)
        postgres_repository.insert_row(mapper(cashback))
    except ValueError:
        raise invalidate_sum_total
    return cashback


def _validate_sum_total(cashback: schemas.CashBack):
    total = cashback.total
    sum_total_products = 0
    
    for product in cashback.products:
        sum_total_products += product.value
    
    if total != sum_total_products:
        raise ValueError
    return True
