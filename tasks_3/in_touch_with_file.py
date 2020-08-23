try:
    with open('text.txt', 'x', encoding='utf8') as textfile:
        text = 'text'
        textfile.write(text)
except:
    print('there is the same')