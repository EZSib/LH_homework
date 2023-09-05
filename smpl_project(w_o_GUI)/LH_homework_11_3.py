'''** В консольном приложении из второго задания добавьте возможность перезаписи (‘w’) и очистки текстового файла.'''

import os

if not os.path.exists('log.txt'):
    with open('log.txt', 'w', encoding='utf8') as f:
        print('log.txt already exists')

with open('log.txt', 'a', encoding='utf8') as date:
    while True:
        text = input('Введите строку для записи\n')
        if text == 'off':
            break
        if text == 'write':
            with open('log.txt', 'w', encoding='utf8') as date:
                while True:
                    text = input('Файл перезаписан\nВведите строку для записи\n')
                    if text == 'off':
                        break
        if text == 'kill':
            print('Данные удалены')
            with open('log.txt', 'w', encoding='utf8') as date:
                break
        print(text, file=date)