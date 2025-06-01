def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX.
    card_number: Номер карты в виде строки.
    """

    # Удаляем пробелы из номера карты
    card_number = card_number.replace(" ", "")

    # Берем первые 6 цифр
    first_part = card_number[:6]

    # Берем последние 4 цифры
    last_part = card_number[-4:]

    # Создаем маску из звездочек для средней части
    middle_part = "** ****"

    # Собираем все вместе в правильном формате
    masked_number = f"{first_part[:4]} {first_part[4:]}{middle_part} {last_part}"

    return masked_number


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета в формате **XXXX.
    account_number: Номер счета в виде строки.
    """

    # Берем последние 4 цифры
    last_part = account_number[-4:]

    # Создаем маску из двух звездочек
    masked_number = f"**{last_part}"

    return masked_number


# Пример использования
if __name__ == "__main__":
    card_number = "7000792289606361"
    print(get_mask_card_number(card_number))  # Вывод: 7000 79** **** 6361

    account_number = "73654108430135874305"
    print(get_mask_account(account_number))  # Вывод: **4305
