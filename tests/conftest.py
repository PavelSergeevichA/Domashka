from typing import Any

import pytest


@pytest.fixture
def card_number_test():
    return "1111222233334444"


@pytest.fixture
def account_number_test():
    return "11112222333344445555"


@pytest.fixture
def full_card_test():
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def full_account_test():
    return "Счет 73654108430135874305"


@pytest.fixture
def empty_str():
    return ""


@pytest.fixture
def zero_data():
    return 0


@pytest.fixture
def date():
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def list_of_users():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]


@pytest.fixture
def empty_list() -> list[Any]:
    return []
