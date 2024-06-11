from typing import Optional


def filter_by_state(operations: list[dict], state: Optional[str] = "EXECUTED") -> list[dict]:
    """Фильтрует транзакции по состоянию"""
    return [elem for elem in operations if elem["state"] == state]


def filter_by_date(operations: list[dict], descending: bool = True) -> list[dict]:
    """Фильтрует транзакции по дате"""
    return sorted(operations, key=lambda date: date.get("date"), reverse=descending)


if __name__ == "__main__":
    print(filter_by_state(operations, state="CANCELED"))
    print(filter_by_date(operations))
