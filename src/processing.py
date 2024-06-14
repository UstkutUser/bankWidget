from typing import Optional


def filter_by_state(operations: list, state: Optional[str] = "EXECUTED") -> list:
    """Фильтрует транзакции по состоянию"""
    return [elem for elem in operations if elem["state"] == state]


def filter_by_date(operations: list, descending: bool = True) -> list:
    """Фильтрует транзакции по дате"""
    return sorted(operations, key=lambda date: date.get("date"), reverse=descending)
