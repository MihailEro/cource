from utils.utils import get_file_operations, get_fixed_data, get_last_operations, get_formatted_data


def main():

    COUNT_LAST_VALUES = 5

    data = get_file_operations()

    data = get_fixed_data(data)
    data = get_last_operations(data, count_last_operations=COUNT_LAST_VALUES)
    data = get_formatted_data(data)

    for row in data:
        print(row, end='\n\n')

if __name__ == '__main__':
    main()
