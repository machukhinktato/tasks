import re
import random
import sys


def abrakadabra(data, name='default.txt'):
    try:
        with open(name, 'x', encoding='utf8') as textfile:
            print('This is my practical work\n', data, file=textfile, end='\n')
    except:
        print('file already exists and will be additionally filled')
        with open(name, 'a', encoding='utf8') as textfile:
            print(data, file=textfile, end='\n')
    finally:
        sys.exit()


def random_data_filler():
    numbers = [random.randint(0, 99) for _ in range(10)]
    letters = []
    for i in range(10):
        numbers_of_ascii = [random.randint(65, 122) for _ in range(10)]
        ascii_generator = []
        [ascii_generator.append(
            chr(number_of_letter)) for number_of_letter in numbers_of_ascii]
        letters.append(''.join(ascii_generator))
    file_to_write = list(zip(numbers, letters))
    string_to_write = [str(value) for value in file_to_write]
    i = 0
    while i < len(string_to_write):
        abrakadabra("'\n'".join(string_to_write))
        i += 1
    return 'objective is done'


def data_controller(name='default.txt'):
    with open(name, 'r') as textfile:
        data_to_fix = [row.rstrip() for row in textfile]
        cutter = r'\W+|\d|\_'
        new_data = []
        for i in range(len(data_to_fix)):
            new_data.append("".join(re.split(cutter, data_to_fix[i])))
        for i in range(len(new_data)):
            data_to_fix.clear()
            data_to_fix.append(f"{new_data[i]} {new_data[i]}")
            print(data_to_fix)

    with open('your_fixed_file.txt', 'w', encoding='utf8') as fixedfile:
        i = 0
        while i < len(data_to_fix):
            print(data_to_fix, file=fixedfile, end='\n')
            i += 1


if __name__ == '__main__':
    # random_data_filler()
    data_controller()
