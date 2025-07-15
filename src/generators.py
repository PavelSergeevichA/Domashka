def filter_by_currency(transaction_list: list, currency: str) -> iter:
    """Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)"""

    return (
        transaction
        for transaction in transaction_list
        if currency == transaction["operationAmount"]["currency"]["name"]
    )


def transaction_descriptions(transaction_list: list) -> iter:
    """Возвращает описание каждой операции по очереди"""

    for description in transaction_list:
        yield description["description"]


def card_number_generator(start: int, stop: int) -> iter:
    """Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты"""

    # Убираем пробелы во входных значениях
    start_gen_num = int(str(start).replace(" ", ""))
    end_gen_num = int(str(stop).replace(" ", ""))

    # Исключаем ввод неверного диапазона значений
    if start_gen_num < 1 or end_gen_num > 9999999999999999 or start_gen_num > end_gen_num:
        raise ValueError("Некорректный диапазон значений.")

    for num in range(start_gen_num, end_gen_num + 1):
        # Преобразуем число в строку и дополняем нулями слева до 16 символов
        card_number = str(num).zfill(16)
        # Форматируем номер карты в требуемый формат
        formatted_card_number: str = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_card_number
