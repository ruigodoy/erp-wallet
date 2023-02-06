import pytest
from pydantic.error_wrappers import ValidationError
from app.entrypoint.api.schemas import Customer, Sale, Product


def test_should_raises_exception_when_document_is_invalid():
    with pytest.raises(ValidationError):
        Customer(
            document="wrong-document",
            name="test-name"
        )


def test_should_raises_exception_when_date_is_invalid():
    with pytest.raises(ValidationError):
        Sale(
            sold_at="wrong-date",
            customer=Customer(
                document="0000000000000",
                name="test-name"
            ),
            total=5.0,
            products=[Product(
                type="A",
                value=5.0,
                qty=1
            )]
        )
