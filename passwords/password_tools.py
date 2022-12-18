from random import choice, shuffle, randint
import json

letters_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 'decorated_function',
                 'u', 'v', 'w', 'x', 'y', 'z']
letters_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
chars = letters_lower + letters_upper + numbers + symbols


def password_generator():
    # TODO: create a password composer function to receive exactly the length and type of password needed
    password_letters1 = [choice(letters_lower) for _ in range(randint(4, 5))]
    password_letters2 = [choice(letters_upper) for _ in range(randint(4, 5))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters1 + password_letters2 + password_symbols + password_numbers
    shuffle(password_list)

    return "".join(password_list)


def writing_json_file(file_name, new_data):
    """
    :param file_name: takes only the name without extension. extension is .json
    :param new_data: should be a json formatted data_frame
    :return: None
    """
    with open(f'{file_name}.json', 'w') as data_file:
        json.dump(new_data, data_file, indent=4)


def save_pass_json(website, email, password):
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }

    try:
        with open('data_frame.json', 'r') as data_file:
            # read old data_frame
            data = json.load(data_file)
    except FileNotFoundError:
        writing_json_file('data_frame', new_data)
    else:
        # updating old data_frame
        data.update(new_data)
        with open('data_frame.json', 'w') as data_file:
            # saving updated data_frame
            json.dump(data, data_file, indent=4)


def caesar_cipher(text: str, shift: int, encode=True, decode=False):
    """
    Creates a encrypted text for hiding paswords and other datas
    :param text: the text that will be encoded/decode
    :param shift: amount of side steps to take
    :param encode: true or false direction
    :param decode: true or false direction
    :return: encoded/decoded text
    """

    logo = """           
     ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
    a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
    8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
    "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
     `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
                88             88                                 
               ""             88                                 
                              88                                 
     ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
    a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
    8b         88 88       d8 88       88 8PP""""""" 88          
    "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
     `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                  88                                             
                  88           
    """

    print(logo)

    text = text.lower()
    shift = int(shift)
    alt_alphabet = []
    cipher_text = ""

    for item in chars:
        alt_alphabet.append(item)

    for letter_index in range(shift):
        alt_alphabet.append(alt_alphabet[0])
        alt_alphabet.remove(alt_alphabet[0])

    if encode:

        for letter in text:
            position = chars.index(letter)
            cipher_text += alt_alphabet[position]

    elif decode and not encode:
        for letter in text:
            position = alt_alphabet.index(letter)
            cipher_text += chars[position]

    return cipher_text



