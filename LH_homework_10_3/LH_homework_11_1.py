'''Создайте консольное приложение, которое позволит дополнять (‘a’) данные в файл log.txt.
Пользователь вводит информацию до тех пор, пока не введет “off”.

Модернизируйте приложение из предыдущей задачи.
Ввод текста в .txt файл должен происходить через графическое приложение tkinter.

** В консольном приложении из второго задания добавьте возможность перезаписи (‘w’) и очистки текстового файла.'''

import os

if not os.path.exists('log.txt'):
    with open('log.txt', 'w', encoding='utf8') as f:
        print('log.txt already exists')

with open('log.txt', 'a', encoding='utf8') as date:
    while True:
        text = input('Введите строку для записи\n')
        if text == 'off':
            break
        print(text, file=date)
