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
