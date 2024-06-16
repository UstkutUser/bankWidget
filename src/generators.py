from src.data import transactions
def filter_by_currency(transactions: list, currency: str) -> iter:
    """Возвращает итератор, который выдает по очереди операции в указанной валюте"""
    return filter(lambda x: x["operationAmount"]["currency"]["name"] == currency, transactions)


usd_transactions = filter_by_currency(transactions, "USD")

try:
    for _ in range(len(transactions)):
        print(next(usd_transactions)["id"])
except StopIteration:
    pass
