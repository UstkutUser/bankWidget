def filter_by_state(transactions: list, state: str="EXECUTED") -> list:
    """Фильтрует транзакции по состоянию"""
    return [elem for elem in transactions if elem["state"] == state]


def filter_by_date(transactions: list, ascending: bool = False) -> list:
    """Фильтрует транзакции по дате"""
    return sorted(transactions, key=lambda date: date.get("date"), reverse=ascending)


transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
     ]

if __name__ == "__main__":
    print(filter_by_state(transactions, state="CANCELED"))
    print(filter_by_date(transactions))