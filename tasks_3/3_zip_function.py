import sys


def zip_function(*args):
    if args:
        keys, values = args
    else:
        keys = task_former()
        values = task_former()
    keys, values = list(keys), list(values)
    if len(keys) > len(values):
        additional_values = len(keys) - len(values)
        for value in range(additional_values):
            values.append(None)
            return dict(zip(keys, values))
    else:
        return dict(zip(keys, values))


def task_former():
    value = 0
    values = []
    print('Инструкция(напоминание):\n'
          'Создайте список ключей, вводя по одному числу за раз\n'
          'Для перехода к списку значений, нажмите любой буквенный знак\n'
          'Заполняйте список значений аналогично, вторичное использование\n'
          'Любого буквенного символа завершит программу')
    while type(value) != str:
        try:
            value = int(input('Введите число: '))
            values.append(value)
        except:
            return values
            sys.exit()


def get_dictionary(keys, values):
    # alternative version
    values.extend([None] * (len(keys) - len(values)))
    return {key: value for (key, value) in zip(keys, values)}


if __name__ == '__main__':
    # print(zip_function())
    # print(zip_function((1, 2, 3, 4, 5, 6, 7, 8), (1, 2, 2, 3, 4, 5)))
    print(get_dictionary([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 2, 3, 4, 5]))
    # print(zip_function((1, 2, 3, 4, 5, 6), (1, 2, 2, 3, 4, 5)))
    # print(zip_function((1, 2, 3, 4), (1, 2, 2, 3, 4, 5)))
    # print(zip_function(('Маша', 'Миша', 'Едет', 'Крыша', 'Голова-то', 'Из Гашиша'), ('Нет', 'Свободы', 'В', 'Беларуси')))
