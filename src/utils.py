import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


def get_operations(input_file) -> list:
    """ Возвращает список словарей с данными о финансовых транзакциях """
    operations = []
    try:
        with open(input_file, encoding='utf-8') as f:
            operations = json.load(f)
        return operations
    except Exception:
        return operations


def convertation(operation: dict) -> float | None:
    """ Возвращает сумму транзакции (amount) в рублях """

    if operation["operationAmount"]["currency"]["code"] == "RUB":
        return float(operation["operationAmount"]["amount"])

    elif operation["operationAmount"]["currency"]["code"] == "USD":
        url = "https://api.apilayer.com/exchangerates_data/convert"
        payload = {
            "amount": "1",
            "from": "USD",
            "to": "RUB"
        }
        response = requests.get(url, headers={"apikey": API_KEY}, params=payload)
        response_dict = response.json()
        course_usd = int(response_dict["result"])
        return float(operation["operationAmount"]["amount"]) * course_usd

    elif operation["operationAmount"]["currency"]["code"] == "EUR":
        url = "https://api.apilayer.com/exchangerates_data/convert"
        payload = {
            "amount": "1",
            "from": "EUR",
            "to": "RUB"
        }
        response = requests.get(url, headers={"apikey": API_KEY}, params=payload)
        response_dict = response.json()
        course_usd = int(response_dict["result"])
        return float(operation["operationAmount"]["amount"]) * course_usd
    else:
        return None


if __name__ == '__main__':
    input_file = '../data/operations.json'
    operation_list = get_operations(input_file)
    operation = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "EUR",
        "code": "EUR"
      }}}

    print(convertation(operation))
