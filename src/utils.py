import json
import logging
import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('../logs/utils.log', mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_operations(input_file) -> list:
    """ Возвращает список словарей с данными о финансовых транзакциях """
    logger.info(f"Начало обработки файла: {input_file}")
    operations = []
    try:
        with open(input_file, encoding='utf-8') as f:
            operations = json.load(f)
            logger.info("Данные с файла сохранены в словарь")
        return operations
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error("Файл не найден, не удалось распознать содержимое файла")
        return operations


def convertation(operation: dict) -> float | None:
    """ Возвращает сумму транзакции (amount) в рублях """

    url = "https://api.apilayer.com/exchangerates_data/convert"
    currency_code = operation["operationAmount"]["currency"]["code"]
    logger.info("Начало обработки операции")

    if currency_code == "RUB":
        logger.info("Операция в рублях, конвертация не требуется")
        return float(operation["operationAmount"]["amount"])

    payload = {
        "amount": "1",
        "from": currency_code,
        "to": "RUB"
    }

    response = requests.get(url, headers={"apikey": API_KEY}, params=payload)
    response_dict = response.json()
    exchange_rate = float(response_dict["result"])
    logger.info(f"Операция в валюте: {currency_code}, "
                f"запрос на конвертацию отправлен, результат: {response_dict["success"]}")

    return float(operation["operationAmount"]["amount"]) * exchange_rate if currency_code in ["USD", "EUR"] else None
