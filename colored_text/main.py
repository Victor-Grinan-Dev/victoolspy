import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


def black(text=''):
    return f"{Fore.BLACK}{text}"


def red(text=''):
    return f"{Fore.RED}{text}"


def green(text=''):
    return f"{Fore.GREEN}{text}"


def yellow(text=''):
    return f"{Fore.YELLOW}{text}"


def blue(text=''):
    return f"{Fore.BLUE}{text}"


def magenta(text=''):
    return f"{Fore.MAGENTA}{text}"


def cyan(text=''):
    return f"{Fore.CYAN}{text}"


def white(text=''):
    return f"{Fore.WHITE} {text}"


def reset(text=''):
    return f"{Fore.RESET} {text}"


def BLACK(text=''):
    return f"{Back.BLACK}{text}"


def RED(text=''):
    return f"{Back.RED}{text}"


def GREEN(text=''):
    return f"{Back.GREEN}{text}"


def YELLOW(text=''):
    return f"{Back.YELLOW}{text}"


def BLUE(text=''):
    return f"{Back.BLUE}{text}"


def MAGENTA(text=''):
    return f"{Back.MAGENTA}{text}"


def CYAN(text=''):
    return f"{Back.CYAN} {text}"


def WHITE(text=''):
    return f"{Back.WHITE} {text}"


def RESET(text=''):
    return f"{Back.RESET} {text}"


def dim(text=''):
    return f"{Style.DIM} {text}"


def normal(text=''):
    return f"{Style.NORMAL} {text}"


def bright(text=''):
    return f"{Style.BRIGHT} {text}"


def reset_all(text=''):
    return f"{Style.RESET_ALL} {text}"


def text_machine(text=None, color=None, background=None, style=None):
    color_list = [black, red, green, yellow, blue, magenta, cyan, white]
    backgrounds = [BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET]
    style_list = [dim, normal, bright, reset_all]

    if not text:
        text = input('desired text: ')

    if not color:
        print('black, red, green, yellow, blue, magenta, cyan, white, reset')
        color = input('choose a font color: ')

    if not background:
        print('BLACK, RED, GREEN YELLOW, BLUEE, MAGENTA, CYAN, WHITE, RESET')
        background = input('choose a background color: ').upper()

    if not style:
        print('Stayle: DIM, NORMAL, BRIGHT, RESET_ALL')
        style = input('choose a style: ')

    for item in color_list:
        if item.__name__ == color.lower():
            text = item(text).strip()
            break

    for item in backgrounds:
        if item.__name__ == background.upper():
            text = item(text).strip()
            break

    for item in style_list:
        if item.__name__ == style:
            text = item(text).strip()
            break

    return text.strip()


if __name__ == '__main__':
    texto = 'hello'

    # # print(red_taxt_white_back)
    #
    # index = 0
    # for _ in test:
    #     print(test[index](texto))
    #     index += 1

    quote = ' hello'
    print(text_machine(quote, color='black', background='reset', style='bright'))
    print('auto reset')