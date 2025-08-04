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
