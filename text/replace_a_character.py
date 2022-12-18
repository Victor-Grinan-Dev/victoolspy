def replace_character(word: str, old: str, new: str, all_ocurrences):  # , by_index: list = None
    """

    :param word:
    :param old: old character to replace
    :param new: new character desired
    :param all_ocurrences: true for all false for the first found case
    :param by_index: list of indexes where the character shoud be replaces
    :return:
    """
    # if by_index is None:
    #     by_index = []
    if all_ocurrences:
        print(all_ocurrences)
        for character in word:
            if character == old:
                word = word.replace(old, new)
                return word

    # elif by_index:
    #      return "?"

    print(all_ocurrences)
    index = len(word) - 1
    while index >= 0:
        if word[index] == old:
            word = word.replace(old, new, __count=1)
            return word
        index -= 1


if __name__ == '__main__':
    print(replace_character("victor grinan valdes", "v", "b", all_ocurrences=False))
