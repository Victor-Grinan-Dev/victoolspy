def from_list(names_invited: list):
    """

    :param names_invited: list object
    :return:
    """
    for guess in names_invited:
        file_name = f'./output/ready_to_send/letter_for_{guess.strip()}.txt'
        with open(file_name, 'w') as letter:
            with open(r'./input/Letters/starting_letter.txt', 'r') as text:
                invitation = text.read()
                final_invitation = invitation.replace('[name]', guess)

            letter.write(final_invitation)
    return 0


def from_txt_document(names_invited: str):
    """

    :param names_invited: address of the document
    :return: None
    """
    with open(names_invited, 'r') as guess_list:
        list_of_names = guess_list.readlines()

        from_list(list_of_names)
    return 0
