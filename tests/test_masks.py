import pytest

from src.masks import mask_account, mask_card


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("7000123412345678", "7000 12** **** 5678"),
        ("1999432189600989", "1999 43** **** 0989"),
    ],
)
def test_mask_card(card_number, expected):
    assert mask_card(card_number) == expected


def test_card_number_1(card_number_1):
    assert mask_card(card_number_1) == "7000 79** **** 6361"


def test_card_number_2(card_number_2):
    assert mask_card(card_number_2) == "7000 12** **** 5678"


def test_card_number_3(card_number_3):
    assert mask_card(card_number_3) == "1999 43** **** 0989"


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("64686473678894779589", "**9589"),
        ("35383033474447895560", "**5560"),
        ("73654108430135874305", "**4305"),
    ],
)
def test_mask_account(account_number, expected):
    assert mask_account(account_number) == expected


def test_account_number_1(account_number_1):
    assert mask_account(account_number_1) == "**4305"


def test_account_number_2(account_number_2):
    assert mask_account(account_number_2) == "**9589"


def test_account_number_3(account_number_3):
    assert mask_account(account_number_3) == "**5560"
