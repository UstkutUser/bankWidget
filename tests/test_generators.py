import pytest


from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
)
from src.data import transactions


@pytest.mark.parametrize(
    "transactions, currency, expected",
    [(transactions, "USD", 939719570), (transactions, "USD", 939719570)],
)
def test_filter_by_currency(transactions, currency, expected):
    usd_transactions = filter_by_currency(transactions, "USD")
    assert next(usd_transactions)["id"] == expected


@pytest.mark.parametrize(
    "transactions, expected",
    [(transactions, "Перевод организации")],
)
def test_transaction_descriptions(transactions, expected):
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == expected


@pytest.mark.parametrize(
    "start, stop, expected",
    [(1, 1, "0000 0000 0000 0001")],
)
def test_card_number_generator(start, stop, expected):
    assert next(card_number_generator(start, stop)) == expected
