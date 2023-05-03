import sqlite3
from random import *
conn = sqlite3.connect('data_users.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE  IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT ,
login VARCHAR(32) NOT NULL,
name VARCHAR(32),
surname VARCHAR(32),
phone INTEGER,
email VARCHAR(64),
password VARCHAR(32))''')

def add_user(login, name, surname, phone, email, password):
    params = (login, name, surname, phone, email, password)
    cur.execute('''INSERT INTO users VALUES (NULL, ?, ?, ?, ?, ?, ?)''', params)
    conn.commit()
    print(f'new user is {name}')
    re_add = (input('''1- add another account\n2- add random account\nany other button- exit\n'''))
    if re_add =='1':
        add_user(input('Введите логин\n'),
                 input('Введите имя\n'),
                 input('Введите фамилию\n'),
                 input('Введите телефон\n'),
                 input('Введите емаил\n'),
                 input('Введите пароль\n'))
    elif re_add == '2':
        random_user()

def random_user():
    chars = [chr(i) for i in range(65, 91)]
    nums = [str(i) for i in range(10)]
    shuffle(chars)
    shuffle(nums)
    add_user(''.join([choice(chars) for _ in range(randint(5,15))]),
             ''.join([choice(chars) for _ in range(randint(5,15))]),
             ''.join([choice(chars) for _ in range(randint(5,15))]),
             ''.join([choice(nums) for _ in range(randint(5,11))]),
             ''.join([choice(chars) for _ in range(randint(5,15))]),
             ''.join([choice(chars) for _ in range(randint(5,15))]))

def run():
    select = input('1- create user\nany other button- create random user\n')
    if select == '1':
        add_user(input('Введите логин\n'),
                 input('Введите имя\n'),
                 input('Введите фамилию\n'),
                 input('Введите телефон\n'),
                 input('Введите емаил\n'),
                 input('Введите пароль\n'))
    else:
        random_user()
run()
conn.close()