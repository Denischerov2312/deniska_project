def hi_func():
    print('Hello')


def input_nums():
    n1, n2 = int(input('Ввод первого числа: ')), int(input('Ввод второго числа: '))
    return n1, n2


def minus_nums(n1, n2):
    print(f'{n1}-{n2}={n1-n2}')


def delit_nums(n1, n2):
    print(f'{n1}/{n2}={n1/n2}')


def bye_bye():
    print('пока, пользователь')


if __name__ == '__main__':
    hi_func()
    n1, n2 = input_nums()
    minus_nums(n1, n2)
    delit_nums(n1, n2)
    bye_bye()
