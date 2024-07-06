import requests
import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def currency_conversion(transaction_amount: float, currency: str) -> float:
    """Конвертирует сумму операции в рубли"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={'RUB'}&from={currency}&amount={transaction_amount}"
    response = requests.get(url, headers={"apikey": API_KEY})
    if response.status_code != 200:
        return 0.0
    data_json = response.json()
    return data_json["result"]


# if __name__ == '__main__':
#     print(currency_conversion(1.0, "EUR"))
