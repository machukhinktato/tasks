def zip_function(*args):
    keys, values = list(args)
    return dict(zip(keys, values))


if __name__ == '__main__':
    print(zip_function((1,2,3,4,5,6),(1,2,2,3,4,5)))