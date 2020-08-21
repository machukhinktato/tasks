import re


def type_checker():
    value = input('Введите число: ')
    if value.isdecimal():
        return f'{int(value)} это целое число.'
    elif value.isalpha():
        return f'{value} это буквенные символы/слово, программа работает только с целыми и дробными числами.'
    else:
        a, b = value.split('.')
        if a == b:
            return f'Число {float(value)} дробное.\nЛевая и правая части совпадают'
        else:
            return f'Число {float(value)} дробное. \nЛевая и правая части не совпадают'


if __name__ == '__main__':
    print(type_checker())
    # print(type_checker('3.14'))
    # print(type_checker('3'))
    # print(type_checker('Lenin'))
