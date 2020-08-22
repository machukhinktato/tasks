def zip_function(*args):
    keys, values = args
    keys, values = list(keys), list(values)
    if len(keys) > len(values):
        additional_values = len(keys) - len(values)
        for value in range(additional_values):
            values.append(None)
        return dict(zip(keys, values))


if __name__ == '__main__':
    print(zip_function((1, 2, 3, 4, 5, 6, 7, 8), (1, 2, 2, 3, 4, 5)))
