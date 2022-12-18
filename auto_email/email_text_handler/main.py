names_invited = r'./Input/Names/names_invited.txt'
starting_letter = r'./input/Letters/starting_letter.txt'

with open(names_invited, 'r') as guess_list:
    for guess in guess_list.readlines():  # the readlines() method includes \n in the items
        file_name = f'./output/ReadyToSend/letter_for_{guess.strip()}.txt'
        with open(file_name, 'w') as letter:
            with open(r'starting_letter.txt', 'r') as text:
                invitation = text.read()
                final_invitation = invitation.replace('[name]', guess)

            letter.write(final_invitation)


