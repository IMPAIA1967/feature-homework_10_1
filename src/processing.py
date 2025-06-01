def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция фильтрует список словарей, оставляя только те, где ключ state равен заданному значению.
    data: Список словарей, которые нужно отфильтровать.
    state: Значение, по которому фильтруем (по умолчанию 'EXECUTED').
    """
    filtered_list = []
    for item in data:
        if item.get('state') == state:
            filtered_list.append(item)
    return filtered_list


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    return sorted(data, key=lambda x: x["date"], reverse=reverse)


"""Сортирует список словарей по ключу 'date'"""

if __name__ == "__main__":
    data = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

    print("Отфильтрованные EXECUTED:")
    print(filter_by_state(data))

    print("\nОтсортированные по дате:")
    print(sort_by_date(data))
