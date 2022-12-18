import os


def check_if_exist_path(path):
    return os.path.exists(path)


def check_if_exist_path_dir(path):
    return os.path.isdir(path)


def check_if_exist_path_file(path):
    return os.path.isfile(path)


def create_file(filename):
    with open(filename, 'w') as file:
        file.write(filename)


def rename_file(old_name, new_name):
    os.rename(old_name, new_name)


def delete_file(dir_name):
    os.rmdir(dir_name)