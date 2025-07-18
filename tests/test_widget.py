from src.widget import get_date, mask_account_card


def test_mask_account_card(full_card_test, full_account_test, empty_str, zero_data):
    assert mask_account_card(full_card_test) == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card(full_account_test) == "Счет **4305"
    assert mask_account_card(empty_str) is None
    assert mask_account_card(zero_data) is None


def test_get_date(date, empty_str, zero_data):
    assert get_date(date) == "11.03.2024"
    assert get_date(empty_str) is None
    assert get_date(zero_data) is None
