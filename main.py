
from math_python import stepen


def hi_func(name):
    print(f'Hello, {name}')


def input_nums():
    n1, n2 = int(input('Ввод первого числа: ')), int(input('Ввод второго числа: '))
    return n1, n2


def minus_nums(n1, n2):
    print(f'{n1}-{n2}={n1-n2}')


def get_name():
    return input('Введите ваше имя: ')


def delit_nums(n1, n2):
    print(f'{n1}/{n2}={n1/n2}')


def bye_bye():
    print('пока, пользователь')


if __name__ == '__main__':
    hi_func(get_name())
    n1, n2 = input_nums()
    minus_nums(n1, n2)
    delit_nums(n1, n2)
    print(stepen(n1, 2))
    bye_bye()
    # Функция принимает два числа и выводит их умножение и деление, и квадрат второго