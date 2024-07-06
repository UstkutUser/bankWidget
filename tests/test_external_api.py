from unittest.mock import patch

from src.external_api import currency_conversion


@patch("src.external_api.requests.get")
def test_currency_conversion(mocked_get):
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "EUR", "to": "RUB", "amount": 1},
        "info": {"timestamp": 1720117264, "rate": 96.217531},
        "date": "2024-07-04",
        "result": 96.217531,
    }
    result = currency_conversion(1.0, "EUR")
    assert result == 96.217531


@patch("src.external_api.requests.get")
def test_currency_conversion_invalid(mocked_get):
    mocked_get.return_value.status_code = 404
    result = currency_conversion(1.0, "EUR")
    assert result == 0.0
