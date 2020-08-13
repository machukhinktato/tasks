import random


def random_nums_generator(lesser_value, greater_value):
    """ handmade number generator"""
    if lesser_value > greater_value:
        lesser_value, greater_value = greater_value, lesser_value
    random_numeric_list, random_numeric_dict, counter = [], {}, 1
    while counter <= greater_value:
        if lesser_value != 0 and greater_value != 0:
            our_number = random.randint(lesser_value, greater_value)
            random_numeric_list.append(our_number)
            random_numeric_dict.update({"elem_" + str(our_number): our_number})
            counter += 1
        else:
            raise ValueError
    print(random_numeric_list)
    print(random_numeric_dict)


def gen_func(start, finish):
    """alternative version"""
    new_lst = []
    new_dict = {}
    for _ in range(10):
        print(finish - start)
        print(random.random())
        print(start)
        rnd = int((finish - start) * random.random() + start)
        print(rnd)
        new_lst.append(rnd)
        new_dict.update({f'elem_{rnd}': rnd})

    return new_lst, new_dict


if __name__ == '__main__':
    # random_nums_generator(10, 1)
    print(gen_func(7, 26))
