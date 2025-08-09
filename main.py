from src.generators import filter_by_currency
from src.open_files import get_transactions_csv, get_transactions_excel, normalize_transaction
from src.processing import filter_by_state, sort_by_date
from src.search_engine import filter_transactions_by_word
from src.utils import get_operations
from src.widget import get_date, mask_account_card

if __name__ == "__main__":
    user_id_list = []
    state = ""

    def filter_by_currency_adapted(transaction_list, currency):
        normalized_transactions = [normalize_transaction(t) for t in transaction_list]
        return filter_by_currency(normalized_transactions, currency)

    # Стартуем! Здороваемся с пользователем. Запрашиваем источник транзакций
    print(
        """Привет! Добро пожаловать в программу работы
с банковскими транзакциями.
Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла"""
    )
    user_type_input = input()

    # Обрабатываем введенные данные, сохраняем нужные данные в список
    if user_type_input == "1":
        print("Для обработки выбран JSON-файл")
        user_id_list = get_operations("data/operations.json")

    elif user_type_input == "2":
        print("Для обработки выбран CSV-файл")
        user_id_list = get_transactions_csv("data/transactions.csv")

    elif user_type_input == "3":
        print("Для обработки выбран XLSX-файл")
        user_id_list = get_transactions_excel("data/transactions_excel.xlsx")

    # Если значение не соответствует предложенным, выводится сообщение, и программа прекращает работу
    else:
        print("Выбран недоступный вариант, попробуйте позже")
        quit()

    # Запрашиваем информацию по фильтрам операций, сохраняем данные в переменную
    while True:
        print(
            """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        )
        statuses = ["EXECUTED", "CANCELED", "PENDING"]
        filter_type = input().upper()
        if filter_type in statuses:
            print(f"Операции отфильтрованы по статусу {filter_type}")
            state = filter_type
            break
        else:
            print(f"Статус операции {filter_type} недоступен.")
            continue
    transactions_list = filter_by_state(user_id_list, state=state)

    # Уточняем параметры сортировки
    print("Отсортировать операции по дате? Да/Нет")
    date_y_n = input()
    print("Отсортировать по возрастанию или по убыванию?")
    in_decrease = input()
    print("Выводить только рублевые транзакции? Да/Нет")
    only_rub = input()
    print(
        "Отфильтровать список транзакций по определенному слову в описании?\n"
        "Если да - введите слово или фразу, если нет - оставьте поле пустым"
    )  #
    keyword = input()
    print("Распечатываю итоговый список транзакций...")

    # Фильтруем и сортируем операции по выбранным параметрам
    if in_decrease.lower() == "по возрастанию":
        reverse = True
    else:
        reverse = False
    if date_y_n.lower() == "да":
        transactions_list_by_date = sort_by_date(transactions_list, reverse=reverse)
    else:
        transactions_list_by_date = transactions_list

    if only_rub.lower() == "да":
        transactions_list_by_currency = filter_by_currency_adapted(transactions_list_by_date, currency="RUB")
    else:
        transactions_list_by_currency = transactions_list_by_date

    if not transactions_list_by_currency:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        quit()

    # Фильтруем список операция по ключевым словам пользователя
    sorted_list = filter_transactions_by_word(transactions_list_by_currency, keyword)

    # Производим окончательную обработку списка и выводим данные пользователю
    print(f"Всего банковских операций в выборке: {len(sorted_list)}\n")
    for transaction in sorted_list:
        print(get_date(transaction.get("date")), transaction.get("description"))
        if not transaction.get("from"):
            print(mask_account_card(transaction.get("to")))
        elif not transaction.get("to"):
            print(mask_account_card(transaction.get("from")))
        else:
            print(mask_account_card(transaction.get("from")), "->", mask_account_card(transaction.get("to")))
        if user_type_input == "1":
            print(
                f"Сумма: {transaction['operationAmount']['amount']} "
                f"{transaction['operationAmount']['currency']['name']}"
            )
        else:
            print(f"Сумма: {transaction.get('amount')} {transaction.get('currency_name')}\n")
