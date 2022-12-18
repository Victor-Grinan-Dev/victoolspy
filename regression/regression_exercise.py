def regression(x):
    if x > 0:
        regression(x - 1)
    print(x)


if __name__ == '__main__':
    regression(5)
