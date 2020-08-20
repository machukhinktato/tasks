import re


def name_holder(path):
    """function which shown file name from path provided"""
    pattern = r'\\+|/|\.'
    result = re.split(pattern, path.lower())
    return result[-2]


if __name__ == '__main__':
    print(name_holder('../mainapp/views.py'))
    print(name_holder('../cmd.exe'))
    print(name_holder('../boot.strap.js'))
    print(name_holder('~//setup.exe'))
    print(name_holder('C:\\IT\\PythonProjects\\tasks\\palindrome.py'))
