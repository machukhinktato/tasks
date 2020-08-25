import random
import os
import re
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


def print_text_file(desc):
    f_in = open(desc.name, 'r')
    f_out = open('second_file.txt', 'w')

    for line in f_in:
        numb = re.search(r'\d*', line)
        string = re.search(r'\s\w*', line)
        line = line.replace(numb.group(0), string.group(0))
        f_out.write(line)

    f_in.close()
    f_out.close()

    with open('second_file.txt', encoding='utf8') as descr:
        for elem in descr:
            print(elem)


DESCRIPTOR = create_text_file('default.txt')

if __name__ == '__main__':
    print_text_file(DESCRIPTOR)