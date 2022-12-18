import os
from datetime import datetime


def os_methods():
    all_ = dir(os)
    for item in all_:
        print(item)


def os_path_methods():
    all_ = dir(os.path)
    for item in all_:
        print(item)


def printdir_change_printdir(new_address):
    print(os.getcwd())
    os.chdir(new_address)
    print(os.getcwd())


def create_dir(dir_name):
    if "\\" in dir_name:
        os.makedirs(dir_name)
    else:
        os.mkdir(dir_name)


def check_if_path_exists(path):
    return os.path.exists(path)


def check_if_path_dir(path):
    return os.path.isdir(path)


def check_if_path_file(path):
    return os.path.isfile(path)


def create_file(filename):
    with open(filename, 'w') as file:
        file.write(filename)


def delete_dir(dir_name):
    os.rmdir(dir_name)


def rename_dir_or_file(old_name, new_name):
    os.rename(old_name, new_name)


def info_(dir_name):
    os.stat(dir_name)


def size_of(dir_name):
    print(os.stat(dir_name).st_size)


def last_modified_date(dir_name):
    mod_time = os.stat(dir_name).st_mtime
    print(datetime.fromtimestamp(mod_time))
    return mod_time


def display_all_dir_tree(dir_name_start):
    for dirpath, dirnames, filenames in os.walk(dir_name_start):
        print('current path:', dirnames)
        print(' files', filenames)
        print()


def display_home_env(env_var=None):
    if not env_var:
        print(os.environ)
    else:
        print(os.environ.get(env_var))


def join_address_path(path_to_file, doc_or_file):
    file_path = os.path.join(path_to_file + doc_or_file)
    print(file_path)
    return file_path


def split_extension_of_file(path):
    result = os.path.splitext(path)
    print(result)
    return result


if __name__ == '__main__':
    # methods()

    # address = "papi\\surprise"
    address = "papi"
    # display_all_dir_tree(address)
    display_home_env()
