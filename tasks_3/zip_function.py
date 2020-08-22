def zip_function(*args):
    # choise = 'n'
    # wish_to_stop, key_list = None, []
    # while choise != wish_to_stop:
    #     wish_to_stop = input('Требуется объединить данные? y/n ').lower()
    #     if 'y':
    #         key_list.append(int(input('Введите число: ')))
        # return type(key_list)
    first_data = list(args)
    return first_data


if __name__ == '__main__':
    print(zip_function(1,2,3,4,5,6))