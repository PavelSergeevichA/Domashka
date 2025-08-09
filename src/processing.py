from typing import Any


def filter_by_state(user_id_list: list, state: str = "EXECUTED") -> list[Any] | None:
    """Возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению"""

    filter_user = []
    for user_id in user_id_list:
        if user_id.get("state") == state:
            filter_user.append(user_id)
        else:
            continue
    return filter_user


def sort_by_date(user_id_list: list, reverse: bool = False) -> list:
    """Возвращает новый список, отсортированный по дате"""

    return sorted(user_id_list, key=lambda user: user['date'], reverse=reverse)
