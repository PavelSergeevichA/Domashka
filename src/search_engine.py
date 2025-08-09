import re


def process_bank_search(bank_operations: list[dict], search: str) -> list[dict]:
    """Возвращает список словарей с данными о банковских операциях, у которых в описании есть слова из строки поиска"""
    search_result = []
    pattern = search
    for bank_operation in bank_operations:
        if re.search(pattern, bank_operation["description"], flags=re.I):
            print(bank_operation)
            search_result.append(bank_operation)
        else:
            continue
    return search_result


def process_bank_operations(bank_operations: list[dict], categories: list) -> dict:
    """Возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории"""
    category_count = {category: 0 for category in categories}

    for operation in bank_operations:
        description = operation.get("description")
        if description in category_count:
            category_count[description] += 1

    return category_count


def filter_transactions_by_word(transactions: list[dict], word: str):
    sorted_list = []
    for transaction in transactions:
        if re.search(word, transaction["description"], re.IGNORECASE):
            sorted_list.append(transaction)
        else:
            continue
    return sorted_list
