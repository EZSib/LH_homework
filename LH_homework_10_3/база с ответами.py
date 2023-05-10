import sqlite3
from tkinter import *
conn2 = sqlite3.connect('answers_new_data.db')
cur2 = conn2.cursor()
cur2.execute('''CREATE TABLE IF NOT EXISTS answers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    answer VARCHAR NOT NULL
    )''')

cur2.execute('INSERT INTO answers (answer) VALUES (?)', ['b'])
conn2.commit()
cur2.execute('INSERT INTO answers (answer) VALUES (?)', ['a'])
conn2.commit()
cur2.execute('INSERT INTO answers (answer) VALUES (?)', ['b'])
conn2.commit()
cur2.execute('INSERT INTO answers (answer) VALUES (?)', ['c'])
conn2.commit()
cur2.execute('INSERT INTO answers (answer) VALUES (?)', ['b'])
conn2.commit()
cur2.execute('INSERT INTO answers (answer) VALUES (?)', ['a'])
conn2.commit()
cur2.execute('INSERT INTO answers (answer) VALUES (?)', ['c'])
conn2.commit()
cur2.execute('INSERT INTO answers (answer) VALUES (?)', ['b'])
conn2.commit()
cur2.execute('INSERT INTO answers (answer) VALUES (?)', ['b'])
conn2.commit()
