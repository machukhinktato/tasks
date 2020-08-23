import random


def abrakadabra(name='default.txt'):
    try:
        # with open(name, 'x', encoding='utf8') as textfile:
        with open(name, 'w', encoding='utf8') as textfile:
            text = 'test'
            textfile.write(text)
    except:
        print('there is the same')


def randomizer():
    numbers = [random.randint(0, 99) for _ in range(10)]
    letters = []
    for i in range(10):
        numbers_of_ascii = [random.randint(65, 122) for _ in range(10)]
        letras = []
        for i in numbers_of_ascii:
            letras.append(chr(i))
        letters.append(''.join(letras))
    return list(zip(numbers, letters))


if __name__ == '__main__':
    abrakadabra()
    print(randomizer())
