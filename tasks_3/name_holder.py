import os
import re


def name_holder(path):
    """function which shown file name from path provided"""
    pattern_filename = r'\\+|/|\.'
    result = re.split(pattern_filename, path.lower())
    return result[-2]


if __name__ == '__main__':
    print(name_holder('../mainapp/views.py'))
