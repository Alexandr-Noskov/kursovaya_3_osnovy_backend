import pytest

from utils import get_data, get_filtered_data, get_formatted_data, get_last_values


def test_get_data():
    data = get_data('operations.json')
    assert isinstance(data, list)
    assert data is not None
# ispravleniee

def test_get_filtered_data(item):
    assert get_filtered_data(item) == [{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }]


def test_get_values(item):
    data = [elem["date"] for elem in get_last_values(item, 3)]
    assert data == ["2019-08-26T10:50:58.294041", "2019-07-03T18:35:29.512364", "2018-06-30T02:08:58.425572"]


def test_get_formatted_data(item):
    print(get_formatted_data(item))
    assert get_formatted_data(item) == ['26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.',
                                        '03.07.2019 Перевод организации\nMasterCard 7158 30** **** 6758 -> Счет **5560\n8221.37 USD',
                                        '30.06.2018 Перевод организации\nСчет 7510 68** **** 6952 -> Счет **6702\n9824.07 USD']