def open_read_csv(filename):
    filename = check_extension(filename)

    if system.check_if_exist_path(filename):
        with open(filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            for line in csv_reader:
                print(line)
        return True
    return False


def create_line_from_list(list_of_items):
    line = ""
    for item in list_of_items:
        line += str(item) + ","

    return line


def check_extension(filename):
    if '.csv_handler' not in filename:
        filename += '.csv_handler'
    return filename


def create_csv(filename):
    filename = check_extension(filename)
    if not system.check_if_exist_path_file(filename):
        with open(filename, 'w') as csv_file:
            csv.writer(csv_file)
            return True
    return False


import csv
from csv_handler.research import os_funcs as system


def add_line(filename, arguments):
    filename = check_extension(filename)

    if type(arguments) == list:
        arguments = create_line_from_list(arguments)

    if not system.check_if_exist_path_file(filename):
        create_csv(filename)

    with open(filename, 'a') as file:
        file.write(arguments)
    return True


def remove_csv(filename):
    if system.check_if_exist_path(filename):
        system.delete_file(filename)


def read_from_csv_as_dictionary(filename):
    with open(filename, 'r') as file:
        data_ = csv.DictReader(file)
        return data_
