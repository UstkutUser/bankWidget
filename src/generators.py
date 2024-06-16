from typing import Generator, Dict


def filter_by_currency(
    transactions: list[Dict], currency: str = "USD"
) -> Generator[Dict[str, object], None, None]:
    """Возвращает итератор, который выдает по очереди операции в указанной валюте"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(
    transactions: list[Dict],
) -> Generator[Dict[str, object], None, None]:
    """Возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]

