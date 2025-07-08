from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_acc_number: str) -> str | None:
    """Возвращает строку с замаскированным номером карты или счета"""

    if card_acc_number != "" and card_acc_number != 0 and card_acc_number is not None and len(card_acc_number) > 21:
        if card_acc_number[
           :4] == "Счет":  # Проверяем тип платежной системы счет или карта и запускаем нужную функцию для
            account = card_acc_number[5:]  # ее обработки
            return card_acc_number[:5] + get_mask_account(account)
        elif card_acc_number[:4] != "Счет":
            card_acc_number_index = 0
            for i in card_acc_number:  # определяем индекс первой цифры номера карты или счета
                if i.isdigit():
                    card_acc_number_index = card_acc_number.find(i)
                    break
            card_number = card_acc_number[int(card_acc_number_index):]
            return card_acc_number[:card_acc_number_index] + get_mask_card_number(card_number)
        return None
    return None


def get_date(user_date: str) -> str | None:
    """возвращает строку с датой в формате 'ДД.ММ.ГГГГ'"""

    if user_date != "" and user_date != 0 and user_date is not None and len(user_date) > 25:
        return user_date[8:10] + "." + user_date[5:7] + "." + user_date[:4]
    return None
