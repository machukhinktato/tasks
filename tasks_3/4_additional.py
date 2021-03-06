import random
import os
from functools import reduce

LINES_COUNT = STRING_SIZE = 10


def get_random_string():
    return reduce(lambda string, char: string + char,
                  [chr(random.randint(ord('a'), ord('z'))) for _ in range(STRING_SIZE)])


def create_text_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf8') as f_descriptor:
            return f_descriptor

    with open(filename, 'w', encoding='utf8') as f_descriptor:
        numbers = [random.randint(0, 100) for _ in range(LINES_COUNT)]
        strings = [get_random_string() for _ in range(LINES_COUNT)]
        f_descriptor.writelines(
            [f"{number} {string} \n" for number, string in zip(numbers, strings)])
        return f_descriptor


def print_text_file(f_descriptor):
    with open(f_descriptor.name, 'r', encoding='utf8') as descriptor:
        for line in descriptor:
            print(line)


DESCRIPTOR = create_text_file('default.txt')

if __name__ == '__main__':
    print_text_file(DESCRIPTOR)