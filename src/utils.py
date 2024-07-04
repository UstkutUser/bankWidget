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


if __name__ == '__main__':
    transactions = get_transactions_from_file("c:\\python\\bankWidget\\data\\operations.json")
    print(transactions)