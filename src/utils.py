import json
from typing import Dict, Any

"""
Реализуйте функцию, которая принимает на вход путь до JSON-файла и 
возвращает список словарей с данными о финансовых транзакциях. Если файл 
пустой, содержит не список или не найден, функция возвращает пустой список. 
Функцию поместите в модуль utils. 
Файл с данными о финансовых транзациях operations.json поместите в 
директорию data/ в корне проекта."""


def get_transactions_from_file(path: str) -> list[Dict] | Any:
    """Принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            try:
                transactions_data = json.load(file)
            except json.JSONDecodeError:
                print("File processing error")
                return []
    except FileNotFoundError:
        raise FileNotFoundError(f"File {path} not found")
        return []
    return transactions_data


if __name__ == "__main__":
    transactions = get_transactions_from_file(
        "c:\\python\\bankWidget\\data\\operations.json"
    )
    print(transactions)

"""Реализуйте функцию, которая принимает на вход транзакцию 
и возвращает сумму транзакции (amount) в рублях, тип данных — 
float. Если транзакция была в USD или EUR, происходит обращение 
к внешнему API для получения текущего курса валют и конвертации 
суммы операции в рубли. Для конвертации валюты воспользуйтесь 
Exchange Rates Data API: https://apilayer.com/exchangerates_data-api. 
Функцию конвертации поместите в модуль external_api."""


def get_transaction_amount(transaction: Dict) -> float:
    """Функция возвращает сумму транзакции в рублях, при необходимости конвертирует в рубли"""
    if not transaction:
        return 0.0
    elif "operationAmount" in transaction:

        return transaction["operationAmount"].get("amount")


if __name__ == "__main__":
    get_transaction_amount(
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {"name": "руб.", "code": "RUB"},
            },
        }
    )
