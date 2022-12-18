import csv
from datetime import datetime


def lorem_ipsum():
    with open('lorem_ipsum.txt', 'r') as file:
        data = file.readlines()
        data_list = [line.strip().split() for line in data]
        list_of_csv = [item for item in data_list]
        return list_of_csv


def create_csv(file_name, data=None):
    with open(f'{file_name}.csv_handler', 'w') as file:
        if not data:
            data = lorem_ipsum()
            for item in data:
                print(item)
                file.write(item)


print(lorem_ipsum())
# print(directorio(csv_handler))
# ---------------- socratica -----------------------#

path = 'test.csv_handler'  # url


def column_to_date(column_name):
    return datetime.strptime(column_name, '%m%d%y')


def data_to_formatted_date(column_name):
    return column_name.strftime('%m/%d/%y')


def column_to_money(column_name):
    return float(column_name)


def column_to_integer(column_name):
    return int(column_name)


def read_file(file_name):
    with open(file_name, newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  # the first line is the header


def write_csv(file_name, data):
    with open(file_name, 'W') as file:
        writer = csv.writer(file)
        writer.writerows(data)
