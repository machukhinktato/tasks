def type_checker():
    """program to check which type of number provided and return info about it"""
    try:
        value = input('Введите число: ')
        if value.isdecimal():
            return f'{int(value)} это целое число.'
        elif value.isalpha():
            return f'{value} это буквенные символы/слово.\n' \
                   f'Программа работает только с целыми и дробными числами.\n' \
                   f'Пограмма завершена.'
        else:
            a, b = value.split('.')
            if a == b:
                return f'Число {float(value)} дробное.\nЛевая и правая части совпадают.'
            else:
                return f'Число {float(value)} дробное. \nЛевая и правая части не совпадают.'
    except:
        return 'Вы указали что-то непонятное, программа завершена'


def compare_parts(parameters):
    try:
        number = float(parameters)
        if int(number) == number:
            return f'{parameters} tseloe chislo'
        print(f'chislo{parameters} drobnoe')
        left,right = parameters.split('.')
        if left == right:
            return 'yes'
        return 'no'
    except:
        ValueError
        return 'not number'


if __name__ == '__main__':
    print(type_checker())
    # print(compare_parts(11))