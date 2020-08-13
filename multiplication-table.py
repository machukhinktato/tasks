def multiplication_former():
    x = int(input('please, enter a first number for multiplication table: '))
    y = int(input('please, enter a second number for multiplication table: '))
    multiplication_builder(x, y)


def multiplication_builder(x, y):
    for i in range(x + 1):
        for j in range(y + 1):
            if j == 0:
                print(i, end='\t')
                continue
            if i == 0:
                print(j, end='\t')
                continue
            else:
                print(i * j, end='\t')
        print('')


def multiplication_table(length, height):
    """ alternative version """
    for i in range(length + 1):
        row = []
        for j in range(height + 1):
            if i == 0:
                row.append(j)
            elif j == 0:
                row.append(i)
            else:
                row.append(i * j)
        print('\t'.join([str(i) for i in row]))


if __name__ == '__main__':
    # multiplication_former()
    multiplication_table(10, 10)
