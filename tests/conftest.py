import pytest


@pytest.fixture
def card_number_1():
    return "7000792289606361"


@pytest.fixture
def card_number_2():
    return "7000123412345678"


@pytest.fixture
def card_number_3():
    return "1999432189600989"


@pytest.fixture
def account_number_1():
    return "73654108430135874305"


@pytest.fixture
def account_number_2():
    return "64686473678894779589"


@pytest.fixture
def account_number_3():
    return "35383033474447895560"


@pytest.fixture
def operations_list():
    client_operations = (
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    )
    return client_operations


@pytest.fixture
def data():
    return "2018-07-11T02:26:18.671407"