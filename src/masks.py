def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты звездочками, отображаются только первые 6 и последние 4 цифпы"""

    if card_number != "" and len(card_number) == 16 and card_number is not None:
        masked_card_number = (card_number[:4], card_number[4:6] + "**", "****", card_number[12:])

        return " ".join(masked_card_number)

    else:
        return "Введите номер карты"


def get_mask_account(account: str) -> str:
    """Маскирует номер банковского счета"""

    if account != "" and account is not None:
        return "**" + account[-4:]
    else:
        return "Введите номер счета"
