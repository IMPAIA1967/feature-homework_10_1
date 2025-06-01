def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX.
    """
    # Удаляем пробелы из номера карты
    card_number = card_number.replace(" ", "")

    # Берем первые 6 цифр и последние 4 цифры
    first_part = card_number[:6]
    last_part = card_number[-4:]

    # Создаем маску
    masked_number = f"{first_part[:4]} {first_part[4:]} ** **** {last_part}"

    return masked_number


def mask_account_number(account_number: str) -> str:
    """
    Маскирует номер счета в формате **XXXX.
    """
    # Берем последние 4 цифры
    last_part = account_number[-4:]

    # Создаем маску
    masked_number = f"**{last_part}"

    return masked_number


def mask_account_card(info: str) -> str:
    """
    Обрабатывает информацию о карте или счете и возвращает замаскированный номер.
    """
    # Разделяем строку на тип и номер
    parts = info.split()
    type_part = parts[0]  # Тип (Visa, Maestro, Счет)
    number_part = parts[-1]  # Номер (последний элемент строки)

    # Проверяем тип и вызываем соответствующую функцию маскировки
    if type_part.lower() in ["visa", "maestro"]:  # Это карта
        return mask_card_number(number_part)
    elif type_part.lower() == "счет":  # Это счет
        return mask_account_number(number_part)
    else:
        return "Неизвестный тип"


# Пример использования
if __name__ == "__main__":
    card_info = "Visa 7000792289606361"
    print(mask_account_card(card_info))  # Вывод: 7000 79** **** 6361

    account_info = "Счет 73654108430135874305"
    print(mask_account_card(account_info))  # Вывод: **4305


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата '2024-03-11T02:26:18.671407' в формат '11.03.2024'.
    """
    # Разбиваем строку по символу 'T' и берем только дату (первую часть)
    date_part = date_str.split('T')[0]

    # Разбиваем дату по символу '-' на год, месяц и день
    year, month, day = date_part.split('-')

    # Собираем дату в нужном формате 'ДД.ММ.ГГГГ'
    formatted_date = f"{day}.{month}.{year}"

    return formatted_date


# Пример использования
if __name__ == "__main__":
    input_date = "2024-03-11T02:26:18.671407"
    print(get_date(input_date))  # Вывод: 11.03.2024
