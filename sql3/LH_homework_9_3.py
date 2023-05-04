import sqlite3
from random import *
import time

conn = sqlite3.connect('data_users.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE  IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT ,
login  VARCHAR(32) NOT NULL,
name VARCHAR(32),
surname VARCHAR(32),
phone INTEGER,
email VARCHAR(64),
password VARCHAR(32)
)''')


def add_user(login, name, surname, phone, email, password):
    params = (login, name, surname, phone, email, password)
    cur.execute('''INSERT INTO users VALUES (NULL, ?, ?, ?, ?, ?, ?)''', params)
    conn.commit()
    print(f'new user is {name}')
    re_add = (input('''1- add another account\n2- add random account\n3-log in\nany other button- exit\n'''))
    if re_add == '1':
        add_user(input('Введите логин\n'),
                 input('Введите имя\n'),
                 input('Введите фамилию\n'),
                 input('Введите телефон\n'),
                 input('Введите емаил\n'),
                 input('Введите пароль\n'))
    elif re_add == '2':
        random_user()
    elif re_add == '3':
        log_in()


def random_user():
    chars = [chr(i) for i in range(65, 91)]
    nums = [str(i) for i in range(10)]
    shuffle(chars)
    shuffle(nums)
    add_user(''.join([choice(chars) for _ in range(randint(5, 15))]),
             ''.join([choice(chars) for _ in range(randint(5, 15))]),
             ''.join([choice(chars) for _ in range(randint(5, 15))]),
             ''.join([choice(nums) for _ in range(randint(5, 11))]),
             ''.join([choice(chars) for _ in range(randint(5, 15))]),
             ''.join([choice(chars) for _ in range(randint(5, 15))]))


def log_in():
    while True:
        try:
            login = input('Введите логин\n')
            cur.execute('SELECT * FROM users WHERE login = ?', (login,))
            log_on = cur.fetchone()[2:]
            break
        except:
            print('Пользователя с таким логином не существует')
    while True:
        try:
            password = input(f'{log_on[0]} введите ваш пароль\n')
            if password == log_on[-1]:
                print('accepted')
                break
            else: raise TypeError
        except:
            print('Неверный пароль')
    print(f'С возвращением {log_on[2]} {log_on[1]}!')
    work = input('1-Заниматься делами\nлюбая кнопка - уйти на заслуженный отдых\n')
    cnt = 0
    while work == '1':
        cnt += 1
        workling()
        work = input('1-Заниматься делами\nлюбая кнопка - уйти на заслуженный отдых\n')
    if cnt > 2:
        print('Отдохните наконец, любуясь восходом благодарной вселенной')
        time.sleep(3)
        exit()
    else:
        print('Приятного отдыха!')
        time.sleep(2)
        exit()


def workling():
    print('Вы начали заниматься делами\n')
    time.sleep(randint(3, 6))
    print('Вы сделали много дел\n')
    print('Хотите продолжить?')


def run():
    select = input('1- create user\n2- create random user\nany other button- log in\n')
    if select == '1':
        add_user(input('Введите логин\n'),
                 input('Введите имя\n'),
                 input('Введите фамилию\n'),
                 input('Введите телефон\n'),
                 input('Введите емаил\n'),
                 input('Введите пароль\n'))
    elif select == '2':
        random_user()
    else:
        log_in()


run()
conn.close()


# cur.execute(f'SELECT name, surname FROM (SELECT * FROM users WHERE login = ?, {login,}) WHERE password = ? ', (password,))