import csv
import os

squirrel_file = '../csv_data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'
pokemons_file = '../csv_data/Pokemon.csv'


def read(item):
    with open(item, 'r') as csv_file:
        return csv.reader(csv_file)


def get_heading_from_input():
    print('Input "exit" to quit.')
    heading_list = []
    is_on = True
    while is_on:
        word = input("input heading: ")
        if word == "exit":
            print(heading_list)
            if heading_list:
                return heading_list
            return None
        heading_list.append(word)


def create_heading(file_name=None, heading=None):
    if not file_name:
        file_name = input("input file name: ")
    if ".csv_handler" not in file_name:
        file_name += ".csv_handler"
    if not heading:
        heading = get_heading_from_input()

    with open(file_name, 'w') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerow(heading)


def add_data(file_name, data):
    pass


if __name__ == '__main__':
    create_heading("person.csv_handler")
