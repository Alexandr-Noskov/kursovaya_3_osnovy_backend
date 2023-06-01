from utils import get_data, get_filtered_data, get_formatted_data, get_last_values


def test_get_data():
    data = get_data('operations.json')
    assert len(data) != 7


def test_get_filtered_data():
    data = get_data('operations.json')
    assert len(get_filtered_data(data)) != 6

def test_get_values():
    data = get_data('operations.json')
    assert get_last_values(data, 2)[0]['date'] == "2023-03-23T01:09:46.296404"
    assert len(get_last_values(data, 5)) == 5

def test_get_formatted_data():
    data = get_data('operations.json')
    print(get_formatted_data(data[0]))
    assert get_formatted_data(data[0]) == """2019-08-26 10:50:58.294041 Перевод организации
Maestro 1596 83** **** 5199 -> Счет **9589
31957.58 руб.\n"""