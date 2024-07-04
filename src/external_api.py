import requests


def currency_conversion(transaction_amount: float, currency: str) -> float:
    """Конвертирует сумму операции в рубли"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={'RUB'}&from={currency}&amount={transaction_amount}"
    response = requests.get(url, headers={"api_key": API_KEY})
