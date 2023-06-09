import sqlite3
from tkinter import *
from tkinter import messagebox as mb
import os
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

# добавляем в базу стандартные вопросы
q1 = Question
q1.core = ' 2 + 2 * 2= '
q1.a = '8'
q1.b = '6'
q1.c = '16'
cur1.execute('INSERT INTO questions (question,theme, a, b, c) VALUES (?, ?, ?, ?, ?)', [q1.core,'math', q1.a, q1.b, q1.c])
conn1.commit()
cur1.execute('INSERT INTO questions (question,theme, a, b, c) VALUES (?, ?, ?, ?, ?)', ['3 + 3 * 3 ** 3= ','math', '84', '81', '5832'])
conn1.commit()
cur1.execute('INSERT INTO questions (question,theme, a, b, c) VALUES (?, ?, ?, ?, ?)', ['сколько дней недели в апреле?','math', '30', '7', '31'])
conn1.commit()
cur1.execute('INSERT INTO questions (question,theme, a, b, c) VALUES (?, ?, ?, ?, ?)', ['какие из нижеперечисленных высказываний НЕ относятся к гачи культуре:','mem', '300 bucks', 'COME ON lets go', 'Sorry, i am chicken'])
conn1.commit()
cur1.execute('INSERT INTO questions (question,theme, a, b, c) VALUES (?, ?, ?, ?, ?)', ['на пенек сел...', 'mem', 'Потом встал', 'Касарь должен был отдать', 'Ну раз сел, так и сиди'])
conn1.commit()
cur1.execute('INSERT INTO questions (question,theme, a, b, c) VALUES (?, ?, ?, ?, ?)', ['ну че, как там с деньгами?', 'mem', 'Внес в капитал прожиточного минимума.', 'С какими деньгами?!', 'Ты кому звонишь сопля?!'])
conn1.commit()
cur1.execute('INSERT INTO questions (question,theme, a, b, c) VALUES (?, ?, ?, ?, ?)', ['мы ребята удалые - лазим в щели половые - ?', 'beasts', 'Строители разлившие бетон', 'Сёстры Вачовски', 'Тараканы'])
conn1.commit()
cur1.execute('INSERT INTO questions (question,theme, a, b, c) VALUES (?, ?, ?, ?, ?)', ['Cобака - 3, кошка - 3, корова - 2, петух - 8, Д.А.Медведев - ?', 'beasts', 'Наша страна не раз проходила\n через серьёзные испытания:\n и печенеги её терзали, и половцы', 'Вы держитесь здесь, вам всего доброго,\n хорошего настроения и здоровья!', '5'])
conn1.commit()
cur1.execute('INSERT INTO questions (question,theme, a, b, c) VALUES (?, ?, ?, ?, ?)', ['что появилось раньше, курица или яйцо?','beasts', 'Курица', 'Олды', 'Яйцо'])
conn1.commit()




# def test_1_window():
#     root1 = Tk()
#     root1.geometry('800x800')
#     root1.title('Тест №1')
#     root1.resizable(0, 0)
#     Button(text='Начать тест!', width=800).pack()
#     Button(text='Правила', width=800, command=about) \
#         .pack()
# def about():
#     a = Toplevel()
#     a.geometry('700x700')
#     a['bg'] = 'grey'
#     a.overrideredirect(True)
#     Label(a, text='''В данном тесте вам необходимо выбрать вариант ответа из представленных.
#         За каждый правильный ответ - вам начисляется балл, за каждый неправильный - ваш счетчик неудач увеличивается на 1.
#          Когда значение счетчика неудач превышает 2, вам необходимо исправить ситуацию либо переходить к следующему тесту.
#          Если вы готовы начать испытание тестом №1 нажмите на кнопку "начать тест!".''')\
#         .pack(expand=1)
#     a.after(30000, lambda: a.destroy())