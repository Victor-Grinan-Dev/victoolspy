import random


def possible_strings(string):
    list_of_str = []
    original = string
    word = ''.join(string)

    while word not in list_of_str:
        list_of_str.append(word)
        string = original
        random.shuffle(string)
        word = ''.join(string)

    return list_of_str


def front_back(str):
    new_word = ""
    if len(str) == 1:
        return str
    else:
        word = list(str)
        first = str[0]
        last = str[-1]
        word[0] = last
        word[-1] = first
        for x in word:
            new_word += x
    return new_word


# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

def string_bits(str):
    i = 1
    word = ""
    for char in str:
        if i % 2 != 0:
            word += char
        i += 1
    return word


# Given a string, return the count of the number of times that a substring length 2 appears in the string and also as
# the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

def last2(str):
    # last 2 chars, can be written as str[-2:]
    last2 = str[len(str) - 2:]
    count = 0

    # Check each substring length 2 starting at i
    for i in range(len(str) - 2):
        sub = str[i:i + 2]
        if sub == last2:
            count = count + 1

    return count


# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So
# "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

def string_match(a, b):
    i = 1
    counter = 0
    for char_a in a:
        j = 1
        if i < len(a):
            sector_a = char_a + a[i]
            # print(sector_a)
            i += 1
            if sector_a in b:
                counter += 1
    return counter


# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period
# (.). So "xxyz" counts but "x.xyz" does not.

def xyz_there(str):
    what = False
    i = 0

    print(str)

    if "xyz" in str and len(str) > 1:

        for element in range(str.count("xyz")):

            i = str.find("xyz", i)

            for char in range(len(str)):

                if str.count('xyz'):

                    if str[str.find('xyz', i) - 1] == '.':
                        what = False
                    else:
                        what = True

            i += 2

    return what
