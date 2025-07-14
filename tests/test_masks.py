import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_data, expected", [
    ("1111222233334444", "1111 22** **** 4444"),
    ("", "Введите номер карты")
])
def test_get_mask_card_number(card_data, expected):
    assert get_mask_card_number(card_data) == expected


@pytest.mark.parametrize("account_data, expected", [
    ("11112222333344445555", "**5555"),
    ('', "Введите номер счета")
])
def test_get_mask_account(account_data, expected):
    assert get_mask_account(account_data) == expected
