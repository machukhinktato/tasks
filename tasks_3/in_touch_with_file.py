def abrakadabra(name='default.txt'):
    try:
        # with open(name, 'x', encoding='utf8') as textfile:
        with open(name, 'w', encoding='utf8') as textfile:
            text = 'test'
            textfile.write(text)
    except:
        print('there is the same')


def randomizer():
    pass


if __name__ == '__main__':
    abrakadabra()