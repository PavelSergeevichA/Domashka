def filter_by_state(user_ids: list, state: str = "EXECUTED") -> list:
    """Возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению"""

    filt_users = []
    for user_id in user_ids:
        if user_id['state'] == state:
            filt_users.append(user_id)
        else:
            continue
    return filt_users


def sort_by_date(user_ids: list, reverse: bool = False) -> list:
    """Возвращает новый список, отсортированный по дате"""

    return sorted(user_ids, key=lambda user: user['date'], reverse=reverse)
