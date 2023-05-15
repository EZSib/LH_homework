'''Создайте консольное приложение, которое позволит дополнять (‘a’) данные в файл log.txt.
Пользователь вводит информацию до тех пор, пока не введет “off”.'''
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
