from unittest.mock import patch

from src.utils import get_transaction_amount


def test_get_transaction_amount():
    """Тестирует возврат суммы транзакции в рублях"""
    example = {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "RUB",
                "code": "RUB",
            }
        }
    }
    assert get_transaction_amount(example) == "9824.07"


@patch("src.utils.currency_conversion")
def test_currency_conversion_usd(mocked_conversion):
    mocked_conversion.return_value = 10
    result = get_transaction_amount(
            {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {
                    "amount": "10",
                    "currency": {
                        "name": "RUB",
                        "code": "RUB",
                }
            }
        }
    )
    assert result == "10"