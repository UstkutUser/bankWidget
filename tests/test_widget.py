import pytest

from src.widget import get_data, mask_card_and_account


@pytest.mark.parametrize(
    "acc_number, expected",
    [
        ("Visa Platinum 7000 7922 8960 6361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_card_and_account(acc_number, expected):
    assert mask_card_and_account(acc_number) == expected


@pytest.mark.parametrize(
    "data, expected",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2021-12-11T03:11:35.464546", "11.12.2021"),
        ("1999-11-11T15:55:05.112344", "11.11.1999"),
    ],
)
def test_get_data(data, expected):
    assert get_data(data) == expected


def test_get_data_1(data):
    assert get_data(data) == "11.07.2018"
