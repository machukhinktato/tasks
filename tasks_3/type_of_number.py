import re


def type_checker(testing):
    value = str(testing)
    if value.isdecimal():
        return int(value)
    elif value.isalpha():
        return value
    else:
        return float(value)


if __name__ == '__main__':
    print(type_checker('3.14'))
    print(type_checker('3'))
    print(type_checker('Lenin'))
