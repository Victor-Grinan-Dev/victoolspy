import pandas as pd
import xlsxwriter

SWAPPIE_FOLDER = 'excel_data/swappie_cases'


def test():
    sq_url = 'excel_data/squirrels.xlsx'
    squirrel = pd.read_excel(sq_url)
    sq_df = pd.DataFrame(squirrel)
    for row in sq_df.iterrows():
        print(row)


file_url = 'excel_data/Operations Planner Case - Victor.xlsx'

sheet1 = 'excel_data/excercise1.xlsx'
excel = pd.read_excel(sheet1)
df = pd.DataFrame(excel)

list_column = [column for column in df.columns if 'Unnamed' not in column]
print(list_column)
# ----------- read just the data columns --------------------
search_value = 1/1/2013

search = df.loc[df == search_value]
print(search)
# TODO: create a new file.xlsx in new directorio (swappie) without the confusing data

# TODO: create a text file with the confusing data as plane text
