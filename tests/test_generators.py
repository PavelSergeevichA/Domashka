from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(list_of_transactions):
    expected_result = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]
    result = list(filter_by_currency(list_of_transactions, currency="USD"))
    assert result == expected_result

    expected_result = [
        {
            "id": 111222333,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "98024.07", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Пополнение счета",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "7911.93", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Покупка",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]
    result = list(filter_by_currency(list_of_transactions, currency="RUB"))
    assert result == expected_result


def test_transaction_descriptions(list_of_transactions):
    expected_result = ['Перевод организации', 'Перевод со счета на счет', 'Пополнение счета', 'Покупка']
    result = list(transaction_descriptions(list_of_transactions))
    assert result == expected_result


def test_card_number_generator():
    generator = card_number_generator("152", "155")
    assert next(generator) == "0000 0000 0000 0152"
    assert next(generator) == "0000 0000 0000 0153"
    assert next(generator) == "0000 0000 0000 0154"
    assert next(generator) == "0000 0000 0000 0155"
