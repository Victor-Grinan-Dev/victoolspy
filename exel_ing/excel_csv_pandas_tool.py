import pandas as pd
import csv
import xlsxwriter
import tkinter as tk
from tkinter import filedialog

squirrels_file = 'csv_data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv_handler'
squirrels_file_excel = 'excel_data/squirrels.xlsx'
data_frame = pd.read_csv(squirrels_file)


def data_from_csv(file):
    """
    Reads a csv_handler file into pandas dataframe form.
    :param file: url of the file to read
    :return: a pandas dataframe df
    """
    df = pd.read_csv(file)
    print(df)
    return df


def data_to_csv(from_data, file_name='new_file.csv_handler'):
    data = pd.Dataframe(from_data)
    if '.csv_handler' not in file_name:
        file_name += '.csv_handler'
    data.to_csv(file_name)


def data_from_excel(file):
    """
    Reads an excel file into a pandas dataframe form.
    :param file: url of the file to read
    :return: a pandas dataframe df
    """
    df = pd.read_excel(file)
    print(df)
    return df


def data_to_excel(from_data, to_file_name='excel_data/new_file.xlsx'):
    """
    Creates a new xlsx file.
    :param from_data: it can be a dictionarie or ...
    :param to_file_name: The str name wished
    :return: None
    """

    data = pd.DataFrame(from_data)
    if '.xlsx' not in to_file_name:
        to_file_name += '.xlsx'

    with pd.ExcelWriter(to_file_name) as writer:
        data.to_excel(writer)


def data_from_dict(dictionary):
    """

    :param dictionary:
    :return:
    """
    data = pd.DataFrame(dictionary)
    return data


def data_to_dict(data):
    """

    :param data:
    :return:
    """
    data_dict = data.to_dict()
    print(data_dict)
    return data_dict


def serie_to_list(file_name, serie):  # serie is a column
    """

    :param file_name:
    :param serie:
    :return:
    """
    data = None

    if 'csv_handler' in file_name:
        data = pd.read_csv(file_name)

    elif 'xlsx' in file_name:
        data = pd.read_excel(file_name)

    data_dict = data.to_dict()
    print(data_dict[serie])
    list_column_values = data_dict[serie].to_list()
    return list_column_values


def serie_average(serie):
    """

    :param serie: must be a heading of a data_frame frame in form of data_frame['heading']
    :return: averge of all the values under the key "serie"
    """
    try:
        ave = serie.mean()
        print(ave)
        return serie.mean()
    except ValueError:
        print('The given serie contains 1 or more non numerical values')


def get_headers(data):
    for column in data.columns:
        print(column)
    return data.columns


# ________________POKEMONS DATABASE___________________#
pokemon_file = 'csv_data/Pokemon.csv_handler'
poke_df = pd.read_csv(pokemon_file)


# print(poke_df.head(5))
# print(poke_df.columns)
# print(poke_df[['Name', 'Type 1', 'Type 2', 'Legendary']])
def integer_location(data, row_number):
    """

    :param data: data frame to use
    :param row_number: can be an integer or slice of integers in form 1:4
    :return:
    """
    print(data.iloc[row_number])
    return data.iloc[row_number]


# print(poke_df.iloc[1])


def using_iterrows(data):
    for index, row in data.iterrows():
        print(index, row)


# using_iterrows(poke_df)


def integer_location_of_cell(data, row_number, column_number):
    """

    :param data: data frame in use
    :param row_number: row number
    :param column_number: column number
    :return: the information of the crossing cell
    """
    print(data.iloc[row_number, column_number])
    return data.iloc[row_number, column_number]


def textual_location(data, column_name, search_value):
    """

    :param data: current dataframe
    :param column_name: the name of the column where we search
    :param search_value: the values that we are searching?
    :return: the row in data base as result? or the column
    """
    search = data.loc[data[column_name] == search_value]
    print(search)
    return search


def search_in_row(column_name, column_value):
    print(poke_df[poke_df.column_name == column_value])


def search_values(data, columns_values):  # NOT WORKING
    """
    search = [('Type 1', 'Grass'), ('Type 2', 'poison')]
    search_values(poke_df, search) # calling the function
    :param data: current dataframe
    :param columns_values: list of tuples
    :return:
    """

    top = len(columns_values)
    count = 1
    querry = f"{data}.loc["
    mid_centence = ''
    querry_end = "]"
    if type(columns_values) is list and len(columns_values) > 1:
        for tuple_item in columns_values:
            # print(tuple) # OK
            mid_centence += f'({data}[{tuple_item[0]}] == {tuple_item[1]})'
            # print(querry)
            count += 1
            if count != top:
                mid_centence += ' & '  # use '|'for 'or'

    querry = querry + mid_centence + querry_end
    print(querry)

    # eval(querry)


# textual_location(poke_df, 'Type 1', 'Water')

# DESCRIBE THE DATA FRAME:
# print(poke_df.describe())

# SORTING DATA:
# print(poke_df.sort_values(['Type 1']))
# print(poke_df.sort_values(['Type 1', 'HP']))
# print(poke_df.sort_values(['Type 1', 'HP'], ascending=False))
# print(poke_df.sort_values(['Type 1', 'HP'], ascending=[1, 0]))  # the first value (type 1) of the search is 1(true)
# and the second value (HP) will be 0 (false) ascending

# CHANGING DATA:
# formula = poke_df['HP']+poke_df['Attack']+poke_df['Defense']+poke_df['Sp. Atk']+poke_df['Sp. Def']+poke_df['Speed']
# poke_df['Total'] = formula
# poke_df['Total'] = poke_df.iloc[:, 4:10].amount(axis=1)  # adding all values in the row 4 to 9
# print(poke_df['Total'])
#
# columns_list = list(poke_df.columns.values)
# print(columns_list)
# poke_df = poke_df[columns_list[0:4] + [columns_list[-1]] + columns_list[4:12]]
# print(poke_df)

# DELETE COLUMN DATA:
# poke_df = poke_df.drop(columns='Total')
# print(poke_df.columns)

# CALLING DATA:
# search = poke_df.loc[(poke_df['Type 1'] == 'Grass') & (poke_df['Type 2'] == 'Poison')]
# print(search)

# FILTERING DATA: (IMPORTANT)
# you can use operator of comparison <, >, <=, >=, ==, &, |
new_df = poke_df.loc[(poke_df['Type 1'] == 'Grass') & (poke_df['Type 2'] == 'Poison') & (poke_df['HP'] > 70)]
# # print(new_df)
new_df = new_df.reset_index()

# print(new_df)

# RESET INDEX:
# new_df = new_df.reset_index(drop=True)
# new_df.reset_index(drop=True, inplace=True)
# print(new_df)
# new_df.to_csv('csv_data/new_poke_df.csv_handler')
# for index, file in new_df.iterrows():
#     print(index, file)

# FIND ALL STR THAT CONATAINS SUBSTR:
print(poke_df.loc[poke_df['Name'].str.contains('Mega')])
print(poke_df.loc[~poke_df['Name'].str.contains('Mega')])  # NOT CONTAINS


# ________________________OTHER TESTS___________________#
# get_headers(data_frame)


# # NOTE: Get a column from database: can be called as dict or as method
#
# print(data_frame.X)
# print(data_frame.Y)
# print(data_frame['Location'])
#
# print(data_frame['X'].max()) # Functions of the database
# print(data_frame['X'].min())
# print(data_frame.X.mean()) # Average
#
# # NOTE: Get a row from database: print(data_frame[data_frame['Unique Squirrel ID'] == '30B-AM-1007-04'])  # print
# # the row where squirrel ID is '30B-AM-1007-04' print(data_frame[data_frame.Y == data_frame.Y.max()])  # print the
# # row where Y coord was the max
#
# # NOTE: Get a specific value from a database.
# search = data_frame[data_frame['Unique Squirrel ID'] == '30B-AM-1007-04']


# print(search.X)
# print(search.Y)
# print(search['Primary Fur Color'])
# print(search['Highlight Fur Color'])

# CREATE DATAFRAME from scrach:
# expenses = (
#     ['Rent', 1000],
#     ['Gas', 100],
#     ['Food', 300],
#     ['Gym', 50],
# )
# data_frame1 = pd.DataFrame(expenses)
# print(data_frame1)

# studend_dict = {
#     "students": ['papi', 'mami', 'alma'],
#     "scores": [50, 75, 100]
# }
# data_frame2 = pd.DataFrame(studend_dict)
# print(data_frame2)

# print('\row_number')

# _________ CREATE A EXCEL FILE FROM DATABASE________________#
def test_create_excel():
    grey_squirrels = len(data_frame[data_frame['Primary Fur Color'] == 'Gray'])
    red_squirrels = len(data_frame[data_frame['Primary Fur Color'] == 'Cinnamon'])
    black_squirrels = len(data_frame[data_frame['Primary Fur Color'] == 'Black'])

    squirrel_dict = {
        "Fur color": ['Grey', 'Red', 'Black'],
        'squirrel count': [grey_squirrels, red_squirrels, black_squirrels]
    }
    sq_dataframe = pd.DataFrame(squirrel_dict)
    print(sq_dataframe)
    data_to_excel(squirrel_dict, 'excel_data/squirrel_count')
    # sq_dataframe.to_csv('csv_data/squirrels_count.csv_handler')


# test_create_excel()


# data_from_excel('excel_data/squirrel_count.xlsx')
#

def ui_excel():
    root = tk.Tk()

    canvas1 = tk.Canvas(root, width=300, height=300, bg='lightsteelblue')
    canvas1.pack()

    def getExcel():
        # global df

        import_file_path = filedialog.askopenfilename()
        df = pd.read_excel(import_file_path)
        print(df)

    browse_button_excel = tk.Button(text='Import Excel File', command=getExcel, bg='green', fg='white',
                                    font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 150, window=browse_button_excel)

    root.mainloop()


# import xlsxwriter
#
# workbook = xlsxwriter.Workbook('excel_data/hello.xlsx')
# worksheet = workbook.add_worksheet()
#
# worksheet.write('A1', 'Hello world')
#
# # Create a workbook and add a worksheet.
# workbook = xlsxwriter.Workbook('excel_data/Expenses02.xlsx')
# worksheet = workbook.add_worksheet()
#
# # Add a bold format to use to highlight cells.
# bold = workbook.add_format({'bold': True})
#
# # Add a number format for cells with money.
# money = workbook.add_format({'num_format': '$#,##0'})
#
# # Write some data_frame headers.
# worksheet.write('A1', 'Item', bold)
# worksheet.write('B1', 'Cost', bold)
#
# # Some data_frame we want to write to the worksheet.
# expenses = (
#     ['Rent', 1000],
#     ['Gas', 100],
#     ['Food', 300],
#     ['Gym', 50],
# )
#
# # Start from the first cell below the headers.
# row = 1
# col = 0
#
# # Iterate over the data_frame and write it out row by row.
# for file, cost in expenses:
#     worksheet.write(row, col, file)
#     worksheet.write(row, col + 1, cost, money)
#     row += 1
#
# # Write a total using a formula.
# worksheet.write(row, 0, 'Total', bold)
# worksheet.write(row, 1, '=SUM(B2:B5)', money)
#
# workbook = xlsxwriter.Workbook('excel_data/salaries.xlsx')
# worksheet = workbook.add_worksheet()
#
# workbook.close()

#
# class CsvTool:
#
#     def __init__(self, file_name):
#         self.file_name = file_name
#         self.headers = self.read_csv()[0]
#         self.data = self.read_csv()[1]
#         self.dictionaries = {}
#
#     def read_csv(self):
#         with open(self.file_name, 'r') as csv_file:
#             csv_reader = csv_handler.DictReader(csv_file)
#             data = [line for line in csv_reader]
#             headers = [file for file in data[0]]
#             data = data[1:]
#
#             # print(headers)
#             # for line in data_frame:
#             #     print(line)  # NOTE: use line[index] to select just a column of data_frame
#
#             return headers, data, csv_reader
#
#
# my_file = CsvTool(file)
# print(my_file.headers)
# print()

# def read_csv(file_name, header=True, as_dict=False):
#     with open(file_name, 'r') as csv_file:
#         if as_dict:
#             csv_reader = csv_handler.DictReader(csv_file)
#         else:
#             csv_reader = csv_handler.reader(csv_file)
#
#         if not header:
#             next(csv_reader)  # skips the header
#             data_frame = [line for line in csv_reader]
#             return data_frame
#
#         data_frame = [line for line in csv_reader]
#         headers = [file for file in data_frame[0]]
#         data_frame = data_frame[1:]
#
#         # print(headers)
#         # for line in data_frame:
#         #     print(line)  # NOTE: use line[index] to select just a column of data_frame
#
#         return headers, data_frame, csv_reader
#
#
# def write_csv(new_file_name, field_names, data_frame, as_dict=False):
#     with open(new_file_name, 'w') as new_file:
#         if not as_dict:
#             csv_writer = csv_handler.writer(new_file)
#
#         else:
#             csv_writer = csv_handler.DictWriter(new_file_name, fieldnames=field_names)
#             csv_writer.writeheader()
#
#         for line in data_frame:
#             csv_writer.writerow(line)
#
#
# def copy_csv(file_name, new_file_name):
#     headers = read_csv(file_name)[0]
#     data_frame = read_csv(file_name)[1]
#     write_csv(new_file_name, headers, data_frame, True)


# copy_csv(file, 'new_file.csv_handler')
# print(read_csv(file)[0])
# print(read_csv(file)[1])
# read_csv(file, header=True)
# read_csv(file, as_dict=True)
# read_field_names(file)
# print(read_csv(file)[0])

# dict_data = read_csv(file)[2]
# for line in dict_data:
#     print(line['x'])

def test2():
    df = pd.read_csv('csv_data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv_handler')
    print([df['X'].head(30), df['Y'].head(30)])

    df1 = pd.DataFrame(df)

    with pd.ExcelWriter('excel_data/squirrels.xlsx') as writer:
        df1.to_excel(writer)

# # df = pd.read_csv(file)
#
# columns_headers = [
#     'X',
#     'Y',
#     'Unique Squirrel ID',
#     'Hectare',
#     'Shift',
#     'Date',
#     'Hectare Squirrel Number',
#     'Age',
#     'Primary Fur Color',
#     'Highlight Fur Color',
#     'Combination of Primary and Highlight Color',
#     'Color notes',
#     'Location',
#     'Above Ground Sighter Measurement',
#     'Specific Location',
#     'Running',
#     'Chasing',
#     'Climbing',
#     'Eating',
#     'Foraging',
#     'Other Activities',
#     'Kuks',
#     'Quaas',
#     'Moans',
#     'Tail flags',
#     'Tail twitches',
#     'Approaches',
#     'Indifferent',
#     'Runs from',
#     'OtherInteractions',
#     'Lat/Long',
# ]
#
# row = 0
# col = 0
#
# with open(file, 'r') as csv_file:
#     csv_reader = csv_handler.reader(csv_file)
#     all_data = [line for line in csv_reader]
#     headers = [file for file in all_data[0]]
#     data_frame = [file for file in all_data[1:]]
#
#     with open('excel_data/squirrels.xlsx', 'w') as workbook:
#         writer = xlsxwriter.Workbook()
#         worksheet = writer.add_worksheet()
#
#         for header in headers:
#             worksheet.write(row, col, header)
#             col += 1

# squirrels = 'excel_data/squirrels.xlsx'
# expenses = 'excel_data/Expenses02.xlsx'
#
# df = pd.read_excel(expenses)
# print(df)
