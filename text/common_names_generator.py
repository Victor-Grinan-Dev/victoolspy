from names_generator import data
from random import choice


class NameMe:
    genders = ("f", "m")
    f_names = data.f_names
    m_names = data.m_names
    l_names = data.last_names

    def __init__(self):

        self.name = self.generate()

    @staticmethod
    def generate(gender: str = None, fullname: bool = True, midname: bool = False, thirdname: bool = False):
        mid = None
        name = None
        if not gender:
            gender = choice(NameMe.genders)
        if gender.lower() == "f":
            name = choice(NameMe.f_names)
            # if midname:
            #     mid = choice(self.f_names)
            #     while mid == name:
            #         mid = choice(self.f_names)

        elif gender.lower() == "m":
            name = choice(NameMe.m_names)
        lastname = choice(NameMe.l_names)

        if fullname:
            return f"{name} {lastname}"
        else:
            return f"{name}"

    @staticmethod
    def many_times(n):
        if n > 10000:
            print("10000 max")
            n = 10000
        gen_list = []
        for _ in range(n):
            suggestion = NameMe.generate()
            if suggestion in gen_list:
                repeat_count = 0
                while suggestion in gen_list:
                    repeat_count += 1
                    suggestion = NameMe.generate()
                    if repeat_count == 10:
                        print("_____________")
            else:
                gen_list.append(suggestion)

        return gen_list


if __name__ == "__main__":

    counter = 1
    for character in NameMe.many_times(100000):
        print(counter, character)
        counter += 1