import random


def abrakadabra(name='default.txt'):
    try:
        with open(name, 'w', encoding='utf8') as textfile:
            textfile.write('This is my practical work\n')
    except:
        print('there is the same')


def randomizer():
    numbers = [random.randint(0, 99) for _ in range(10)]
    letters = []
    for i in range(10):
        numbers_of_ascii = [random.randint(65, 122) for _ in range(10)]
        ascii_call = []
        for i in numbers_of_ascii:
            ascii_call.append(chr(i))
        letters.append(''.join(ascii_call))
    banana = list(zip(numbers, letters))
    with open('default.txt', 'a', encoding='utf8') as textfile:
        for i in range(len(banana)):
            textfile.writelines(str(banana[i]) + '\n')
        # return banana[1]

if __name__ == '__main__':
    abrakadabra()
    print(randomizer())
