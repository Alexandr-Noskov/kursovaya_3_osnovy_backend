
from utils import get_data, get_filtered_data, get_last_values, get_formatted_data

filename = 'operations.json'

def main():
    FILTERED_EMPTY_FROM = True
    COUNT_LAST_VALUES = 5

    data = get_data(filename)
    data = get_filtered_data(data, filter_empty_from=FILTERED_EMPTY_FROM)
    data = get_last_values(data, count_last_values=COUNT_LAST_VALUES)
    data = get_formatted_data(data)
    print("INFO: Вывод транзакций...")
    for row in data:
        print(row, end='\n\n')

if __name__ == "__main__":
       main()