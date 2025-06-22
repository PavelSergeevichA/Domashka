from masks import get_mask_card_number, get_mask_account


def mask_account_card(card_acc_number: str) -> str:
    """Возвращает строку с замаскированным номером карты или счета"""

    card_acc_number_index = 0
    for i in card_acc_number:   # определяем индекс первой цифры номера карты или счета
        if i.isdigit():
            card_acc_number_index = card_acc_number.find(i)
            break

    if card_acc_number[:4] == "Счет":   # Проверяем тип платежной системы счет или карта и запускаем нужную функцию для
        account = card_acc_number[5:]   # ее обработки
        return card_acc_number[:5] + get_mask_account(account)
    elif card_acc_number[:4] != "Счет":
        card_number = card_acc_number[int(card_acc_number_index):]
        return card_acc_number[:card_acc_number_index] + get_mask_card_number(card_number)
