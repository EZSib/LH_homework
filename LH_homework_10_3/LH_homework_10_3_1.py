import sqlite3
import hashlib
from tkinter import *
from tkinter import messagebox as mb

conn1 = sqlite3.connect('questions_new_data.db')
cur1 = conn1.cursor()
cur1.execute('''CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question VARCHAR NOT NULL UNIQUE,
    a VARCHAR NOT NULL,
    b VARCHAR NOT NULL,
    c VARCHAR NOT NULL)''')



class Question():
    def __init__(self, core: str, a: str, b: str, c: str):
        self.string = core
        self.a = a
        self.b = b
        self.c = c

q1 = Question
q1.core = ' 2 + 2 * 2= '
q1.a = '8'
q1.b = '6'
q1.c = '16'
cur1.execute('INSERT INTO questions (question, a, b, c) VALUES (?, ?, ?, ?)', [q1.core, q1.a, q1.b, q1.c])
conn1.commit()