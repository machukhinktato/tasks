import random


def random_nums_generator(lesser_value, greater_value):
    if lesser_value > greater_value:
        lesser_value, greater_value = greater_value, lesser_value
    random_numeric, counter = [], 1
    while counter <= greater_value:
        if lesser_value != 0 and greater_value != 0:
            random_numeric.append(random.randint(lesser_value, greater_value))
            counter += 1
        else:
            raise ValueError

    print(random_numeric)


if __name__ == '__main__':
    random_nums_generator(10, 1)
