class stringHandler:
    @staticmethod
    def reverse_word(word):
        revers_list = []
        index = 0
        for char in word:
            revers_list.insert(index, char)
            index += -1
            reverse = ""
        for item in revers_list:
            reverse += item
        return reverse

    @staticmethod
    def replace(str, char, position):
        """this will replace the word of the given string in the given position with the given char
        and returns the new string"""
        str[position] = char
        return str