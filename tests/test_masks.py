from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(card_number_test):
    assert get_mask_card_number(card_number_test) == "1111 22** **** 4444"


def test_get_mask_account(account_number_test):
    assert get_mask_account(account_number_test) == "**5555"
