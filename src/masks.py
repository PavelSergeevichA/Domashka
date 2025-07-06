def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты звездочками, отображаются только первые 6 и последние 4 цифпы"""

    if card_number != "" or len(card_number) == 16 or card_number is not None:
        masked_card_number = (card_number[:4], card_number[4:6] + "**", "****", card_number[12:])

        return " ".join(masked_card_number)

    else:
        return "Введите номер карты"


def get_mask_account(account: str) -> str:
    """Маскирует номер банковского счета"""

    if account != "" or len(account) == 16 or account is not None:
        return "**" + account[-4:]
    else:
        return "Введите номер счета"
