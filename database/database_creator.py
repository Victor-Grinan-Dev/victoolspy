import mysql
import datetime


class DatabaseMage:
    host = "localhost"
    user = "root"
    password = "vitismanXD2019!"

    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        # database=db_name
    )
    mycursor = mydb.cursor()

    @staticmethod  # WORKS DONT TOUCH
    def create_a_db(db_name, host="localhost", user="root", password="vitismanXD2019!"):

        """creates a database with the given name,
         it will use the local host if not specified"""

        DatabaseMage.mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")

    @staticmethod
    def create_table(table_name, header_list, data_types=None):

        """this will create the headers of a table for you
        JUST need table_name(str), header_list(list of str) and
         data_types(a list of:
                    any numbers (for integer data_frame type),
                    any letters (for string data_frame type),
                    a capital "F" (for floating point data_frame type),
                    the string "bool" (for a boolean type)
                    or the string "time" (for a timestamp type)
        WARNING!: needs to be in the same indexing order of eachother
        ie:
        create_table(myTable, ["amount", "object_name", "rated", "last_used_date", "is_broken"], [1,"a","F","time","bool"])"""

        # mycursor = DatabaseMage.mydb.cursor()

        headers = []

        if not data_types:
            print('type:\n-any number for integer\n-any letter for varchar \n-any symbol for float\n-type bool for '
                  'Boolean\n-type time for a time stamp')
            for header in header_list:
                data_type_input = input(f'enter {header} data_frame type: ')
                data_type = DatabaseMage.data_type_validator(data_type_input)
                headers.append([header, data_type])

        else:
            if len(header_list) == len(data_types):
                for index in range(len(header_list)):
                    headers.append([header_list[index], DatabaseMage.data_type_validator(data_types[index])])

        ready_sql_header_query = DatabaseMage.query_table_creation(table_name, headers)
        return ready_sql_header_query  # call execute_table_creation() function

    @staticmethod
    def data_type_validator(data_type_input):

        """creates the right query str ONLY for varchar or integers"""

        data_type_input = str(data_type_input)

        if data_type_input.lower() == "time":
            return "TIMESTAMP"

        elif data_type_input.lower() == "bool":
            return "BOOLEAN"

        elif data_type_input == "F":
            return "DECIMAL (5, 2)"

        elif data_type_input.isdigit():
            return 'INTEGER(10)'

        else:
            return 'VARCHAR(255)'

    @staticmethod
    def booleans_or_float(data):
        pass

    @staticmethod
    def query_table_creation(table_name, headers):

        """finishes the query syntax"""

        query_end = ''
        for i in headers:
            for j in i:
                query_end += f'{j}'
                if j == i[1] and i != headers[-1]:
                    query_end += ''
                elif j == i[1] and i == headers[-1]:
                    return f'CREATE TABLE {table_name} ({query_end})'
                else:
                    query_end += ' '
            query_end += ', '

    @staticmethod
    def sql_formula(table_name, headers):

        """recives: table_name(str) and headers(list of str)
        returns: formula for populating a table (included place holders)
        return ie: INSERT INTO martians (martian_id, first_name, last_name,
        base_id, super_id) VALUES(%s, %s, %s, %s, %s)"""

        mid_str = ''
        place_holders = "%s, " * (len(headers) - 1) + "%s"
        for header in headers:
            mid_str += header
            if header == headers[-1]:
                return f"INSERT INTO {table_name} ({mid_str}) VALUES({place_holders})"
            else:
                mid_str += ', '

    @staticmethod
    def optimaze_data_values(values_list):

        """makes sure that the str "null" values return as sql "null"
        and the rest of the values are str and capitalized"""

        # REQUIERES CODE: (in your script)
        # import database_creator
        # opt_values_list = database_creator.Tables.optimaze_data_values(values_list)

        new_values_list = []
        for val in values_list:
            new_element_list = []
            for element in val:
                if type(element) == int:
                    element = str(element)
                if element.lower() == 'null':
                    element = None  # convert to sql null value
                elif type(element) == str:
                    element = element.capitalize()
                new_element_list.append(element)
            new_values_list.append(tuple(new_element_list))
        return new_values_list

    @staticmethod
    def from_csv_reader_generator(csv_path):

        """yields line by line csv_handler converted to list"""

        with open(csv_path, "r") as csv_file:
            # skip headers
            csv_file.readline()

            index = 0
            for line in csv_file:
                one_line = csv_file.readline()
                if "\n" in line:
                    one_line = one_line.split("\n")[0]

                yield one_line.split(",")

    @staticmethod
    def timestamp_creator(element, time_format="%Y-%m-%d %H:%M:%S"):
        import datetime

        """this will return the exact format needed for your time stamp"""

        return datetime.datetime.strptime(element, time_format)


# AMATEUR TEST
# def create_table(table, headers):
#     mycursor.execute(query_table_creation(table, headers))


martian = ['martian_id', 'first_name', 'last_name', 'base_id', 'super_id']
# print(Table_creator.create_headers('martian', martian,[1,'a','a',1,1]))
base = ['base_id', 'base_name', 'founded']
visitor = ['visitor_id', 'host_id', 'first_name', 'last_name']
inventory = ['base_id', 'supply_id', 'quantity']
supply = ['supply_id', 'name', 'description', 'quantity']
headers = [['martian_id', 'INTEGER(10)'], ['first_name', 'VARCHAR(255)'],
           ['last_name', 'VARCHAR(255)'], ['base_id', 'INTEGER(10)'],
           ['super_id', 'INTEGER(10)']]

path = r"C:\Users\victo\Downloads\london-bikes.csv_handler"

# for file in DatabaseMage.from_csv_reader_generator(path):
#     print(file)

# print(query_table_creation('martians', headers))

# print(Table_creator.sql_formula('martians', martian))
# print(Table_creator.sql_formula('base', base))
# print(Table_creator.sql_formula('visitor', visitor))
# print(Table_creator.sql_formula('inventory', inventory))
# print(Table_creator.sql_formula('supply', supply))
