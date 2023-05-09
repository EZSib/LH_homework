import sqlite3
import hashlib
from tkinter import *
from tkinter import messagebox as mb

conn1 = sqlite3.connect('questions_new_data.db')
cur1 = conn1.cursor()
cur1.execute('''CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question VARCHAR NOT NULL UNIQUE,
    theme VARCHAR NOT NULL,
    a VARCHAR NOT NULL,
    b VARCHAR NOT NULL,
    c VARCHAR NOT NULL)''')



class Question():
    def __init__(self, core: str,theme:str, a: str, b: str, c: str):
        self.string = core
        self.theme = theme
        self.a = a
        self.b = b
        self.c = c

#добавляем в базу стандартные вопросы
q1 = Question
q1.core = ' 2 + 2 * 2= '
q1.a = '8'
q1.b = '6'
q1.c = '16'
cur1.execute('INSERT INTO questions (question,theme, a, b, c) VALUES (?, ?, ?, ?, ?)', [q1.core,'math', q1.a, q1.b, q1.c])
conn1.commit()
cur1.execute('INSERT INTO questions (question,theme, a, b, c) VALUES (?, ?, ?, ?, ?)', ['3 + 3 * 3 ** 3= ','math', 'q1.a', 'q1.b', 'q1.c'])
conn1.commit()
cur1.execute('INSERT INTO questions (question,theme, a, b, c) VALUES (?, ?, ?, ?, ?)', ['сколько дней недели в апреле?','math', '30', '7', '31'])
conn1.commit()
cur1.execute('INSERT INTO questions (question,theme, a, b, c) VALUES (?, ?, ?, ?, ?)', ['какие из нижеперечисленных высказываний НЕ относятся к гачи культуре:','mem', '300 bucks', 'COME ON lets go', 'Sorry, i am chicken'])
conn1.commit()
cur1.execute('INSERT INTO questions (question,theme, a, b, c) VALUES (?, ?, ?, ?, ?)', ['на пенек сел...', 'mem', 'Потом встал', 'Касарь должен был отдать', 'Ну раз сел, так и сиди'])
conn1.commit()
cur1.execute('INSERT INTO questions (question,theme, a, b, c) VALUES (?, ?, ?, ?, ?)', ['ну че, как там с деньгами?', 'mem', 'Это служба безопасности сбербанка,ваши средства в опасности, срочно переведите их на ... безопасный счет!', 'С какими деньгами?!', 'Ты кому звонишь сопля?!'])
conn1.commit()
cur1.execute('INSERT INTO questions (question,theme, a, b, c) VALUES (?, ?, ?, ?, ?)', ['мы ребята удалые - лазим в щели половые - ?', 'beasts', 'Строители разлившие бетон', 'Сёстры Вачовски', 'Тараканы'])
conn1.commit()
cur1.execute('INSERT INTO questions (question,theme, a, b, c) VALUES (?, ?, ?, ?, ?)', ['Cобака - 3, кошка - 3, корова - 2, петух - 8, Д.А.Медведев - ?', 'beasts', 'Наша страна не раз проходила через серьёзные испытания: и печенеги её терзали, и половцы', 'Вы держитесь здесь, вам всего доброго, хорошего настроения и здоровья!', '5'])
conn1.commit()
cur1.execute('INSERT INTO questions (question,theme, a, b, c) VALUES (?, ?, ?, ?, ?)', ['что появилось раньше, курица или яйцо?','beasts', 'Курица', 'Олды', 'Яйцо'])
conn1.commit()


