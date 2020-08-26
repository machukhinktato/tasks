from datetime import datetime


"""how super() works"""


class Person:

    def __init__(self, firstname, secondname):
        self.firstname = firstname
        self.secondname = secondname

    def action(self):
        return print('person action')


class Doctor(Person):
    def __init__(self, firstname, secondname, age):
        super().__init__(firstname, secondname)
        self.age = age

    def action(self):
        super().action()
        return print('doctor action')


"""decorator with fucntions which takes args"""


def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result

    return wrapper


@timer
def matilda(name):
    result = name
    print(f'Hello world from {result}')


if __name__ == '__main__':
    matilda('mike')
    # a = lt('Mike')
    # print(a)
    # a = Person('Misha', 'Tarabrin')
    # b = Doctor('Misha', 'Tarabrin', 32)
    # b.action()
    # print( a.firstname, a.secondname, b.firstname, b.secondname, b.age)
