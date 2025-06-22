def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты звездочками, отображаются только первые 6 и последние 4 цифпы"""

    masked_card_number = (card_number[:4], card_number[4:6] + "**", "****", card_number[12:],)

    return " ".join(masked_card_number)


def get_mask_account(account: str) -> str:
    """Маскирует номер банковского счета"""

    return "**" + account[-4:]
