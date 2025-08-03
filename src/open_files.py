import csv

import pandas as pd


def get_transactions_csv(input_file_csv) -> list:
    """Возвращает список транзакций, загруженный из файла csv"""
    list_of_transactions = []
    with open(input_file_csv, encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            list_of_transactions.append(row)
    return list_of_transactions


def get_transactions_excel(input_file_excel) -> list:
    """Возвращает список транзакций, загруженный из файла excel"""
    df = pd.read_excel(input_file_excel)
    list_of_transactions = df.to_dict(orient='records')
    return list_of_transactions
