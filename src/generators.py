def filter_by_currency(transaction_list: list, currency: str) -> iter:
    """Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)"""

    return (transaction for transaction in transaction_list if currency ==
            transaction["operationAmount"]["currency"]["name"])


def transaction_descriptions(transaction_list: list) -> iter:
    """Возвращает описание каждой операции по очереди"""

    return (description["description"] for description in transaction_list)
