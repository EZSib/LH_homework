import sqlite3

connect = sqlite3.connect('data.db')
cur = connect.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task VARCHAR(128) NOT NULL,
        is_done INTEGER(1) DEFAULT 0 NOT NULL
        )''')
action = input('''Welcome to in \' lists tasks\'
1- print lists tasks
2- add task
3- run task
0 - exit''')
while action != '0':
    if action == '2':
        task = input('print new task')
        cur.execute('INSERT INTO tasks(task) VALUES("' + task + '")')

