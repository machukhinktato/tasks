import random
import sys


def abrakadabra(data, name='default.txt'):
    try:
        with open(name, 'x', encoding='utf8') as textfile:
            print('This is my practical work\n', data, file=textfile, end='\n')
    except:
        print('file already exists and will be added')
        with open(name, 'a', encoding='utf8') as textfile:
            print(data, file=textfile, end='\n')
    finally:
        sys.exit()


def randomizer():
    numbers = [random.randint(0, 99) for _ in range(10)]
    letters = []
    for i in range(10):
        numbers_of_ascii = [random.randint(65, 122) for _ in range(10)]
        ascii_generator = []
        [ascii_generator.append(chr(number_of_letter)) for number_of_letter in numbers_of_ascii]
        letters.append(''.join(ascii_generator))
    file_to_write = list(zip(numbers, letters))
    string_to_write = [f'{str(value)}' for value in file_to_write]
    print(string_to_write)
    while i < len(string_to_write):
        abrakadabra(''.join(string_to_write[i]))
        i += 1
    return 'objective is done'


if __name__ == '__main__':
    randomizer()
