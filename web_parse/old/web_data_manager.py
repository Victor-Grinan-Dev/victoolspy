import os


def txt_creator(army_class, data, title, path):
    os.chdir(path)
    os.mkdir(f'{army_class}')
    os.chdir(army_class)

    with open(f'{title}.txt', 'a') as f:
        sub_data = data.readlines()
        for line in sub_data:
            f.writeline(line)

        # if not army_class in os.listdir():
        #     os.mkdir(f'{army_class}')
        #     os.chdir(army_class)

        # if not f'{title}.txt' in os.listdir(army_class):
        #     with open(f'{title}.txt', 'w') as f:
        #         for line in data:
        #             f.writeline(line)

# with open('one_test.txt','r') as f:
#     for line in f:
#         f_cont = f.readline()
#         print(f_cont, end='')
