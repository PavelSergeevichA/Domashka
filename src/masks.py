import logging

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('../logs/masks.log', mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты звездочками, отображаются только первые 6 и последние 4 цифры"""
    logger.info(f"Получен номер карты: {card_number}")
    if card_number != "" and len(card_number) == 16 and card_number is not None:
        masked_card_number = (card_number[:4], card_number[4:6] + "**", "****", card_number[12:])

        logger.info("Номер карты замаскирован")
        return " ".join(masked_card_number)

    else:
        logger.error(f"Введен номер карты неподходящего формата: {card_number}")
        return "Введите номер карты"


def get_mask_account(account: str) -> str:
    """Маскирует номер банковского счета"""
    logger.info(f"Получен номер счета: {account}")
    if account != "" and account is not None:
        logger.info("Номер счета замаскирован")
        return "**" + account[-4:]
    else:
        logger.info(f"Введен номер счета неподходящего формата: {account}")
        return "Введите номер счета"
