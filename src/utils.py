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
    except (FileNotFoundError, json.JSONDecodeError):
        return operations


def convertation(operation: dict) -> float | None:
    """ Возвращает сумму транзакции (amount) в рублях """

    url = "https://api.apilayer.com/exchangerates_data/convert"
    currency_code = operation["operationAmount"]["currency"]["code"]

    if currency_code == "RUB":
        return float(operation["operationAmount"]["amount"])

    payload = {
        "amount": "1",
        "from": currency_code,
        "to": "RUB"
    }

    response = requests.get(url, headers={"apikey": API_KEY}, params=payload)
    response_dict = response.json()
    exchange_rate = float(response_dict["result"])

    return float(operation["operationAmount"]["amount"]) * exchange_rate if currency_code in ["USD", "EUR"] else None
