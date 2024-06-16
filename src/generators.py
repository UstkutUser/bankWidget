from typing import Dict, Generator


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


def card_number_generator(start, stop):
    for i in range(start, stop + 1):
        num = (16 - len(str(i))) * "0" + str(i)
        yield " ".join(num[i : i + 4] for i in range(0, 16, 4))
