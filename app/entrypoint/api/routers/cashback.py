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
        postgres_repository.insert_row(mapper(sale))
    except ValueError:
        raise invalidate_sum_total
    return sale


def _validate_sum_total(sale: schemas.Sale):
    total = sale.total
    sum_total_products = 0
    
    for product in sale.products:
        sum_total_products += product.value
    
    if total != sum_total_products:
        raise ValueError
    return True
