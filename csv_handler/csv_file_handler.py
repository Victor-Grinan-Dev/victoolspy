import csv
import os
import shutil
from tempfile import NamedTemporaryFile


def get_length(file_path, output=False):
    lenth = 1
    with open(file_path, "r") as csvfile:
        file_reader = csv.reader(csvfile)

        for line in file_reader:
            if output:
                print(lenth, line)
            lenth += 1

    return lenth


def check_if_exist_path(file_path):
    return os.path.exists(file_path)


def check_if_exist_path_dir(file_path):
    return os.path.isdir(file_path)


def check_if_exist_path_file(file_path):
    return os.path.isfile(file_path)


def create_file(filename):
    with open(filename, 'w') as file:
        file.write(filename)


def rename_file(old_name, new_name):
    os.rename(old_name, new_name)


def delete_file(dir_name):
    os.rmdir(dir_name)


def open_read_csv(filename):
    filename = check_extension(filename)

    if check_if_exist_path(filename):
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
    if not check_if_exist_path_file(filename):
        with open(filename, 'w') as csvfile:
            csv.writer(csvfile)
            return True
    return False


def add_line(filename, arguments):
    filename = check_extension(filename)

    if type(arguments) == list:
        arguments = create_line_from_list(arguments)

    if not check_if_exist_path_file(filename):
        create_csv(filename)

    with open(filename, 'a') as file:
        file.write(arguments)
    return True


def remove_csv(filename):
    if check_if_exist_path(filename):
        delete_file(filename)


def remove_line_from_csv():
    pass


def read_from_csv_as_dictionary(filename):
    with open(filename, 'r') as file:
        data_ = csv.DictReader(file)
        return data_


if __name__ == '__main__':
    # class csv_database_handler:
    #
    #     def __init__(self, path):
    #         self.path = path

    file_name = "../csv_handler/csv_data/new_poke_df.csv"
    temp_file = NamedTemporaryFile(delete=False)

    with open(file_name, "rb") as csv_file, temp_file:
        reader = csv.DictReader(csv_file)
