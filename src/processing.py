def filter_by_state(user_ids: list, state="EXECUTED") -> list:
    """Возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению"""

    filt_users = []
    for user_id in user_ids:
        if user_id['state'] == state:
            filt_users.append(user_id)
        else:
            continue
    return filt_users
