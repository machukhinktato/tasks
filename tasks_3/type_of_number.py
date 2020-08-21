def type_checker():
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
                return f'Число {float(value)} дробное.\nЛевая и правая части совпадают'
            else:
                return f'Число {float(value)} дробное. \nЛевая и правая части не совпадают'
    except:
        return 'Вы указали что-то непонятное, программа завершена'


if __name__ == '__main__':
    print(type_checker())