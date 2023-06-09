import sqlite3
import hashlib
from tkinter import *
from tkinter import messagebox as mb
import time
from random import *
from datetime import datetime
import os

try:
    import pandas as pd
    from tabulate import tabulate
except ImportError:
    os.system('pip install pandas')
    os.system('pip install tabulate')
    import pandas as pd
    from tabulate import tabulate

conn = sqlite3.connect('users_new_data.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS list_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login VARCHAR(64) NOT NULL UNIQUE,
    password VARCHAR(64) NOT NULL)''')

con_res = sqlite3.connect('results_new_data.db')
cur_res = con_res.cursor()

cur_res.execute('''CREATE TABLE IF NOT EXISTS results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    login VARCHAR(64) NOT NULL,
                    overall_result INTEGER NOT NULL,
                    percent_result VARCHAR(64) NOT NULL,
                    counter_try VARCHAR(64) NOT NULL,
                    date_start VARCHAR(64) NOT NULL,
                    date_end VARCHAR(64) NOT NULL,
                    time_test VARCHAR(64) NOT NULL)''')

if os.path.exists('answers_new_data.db'):
    pass
else:
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

if os.path.exists('questions_new_data.db'):
    pass
else:
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
        def __init__(self, core: str, theme: str, a: str, b: str, c: str):
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
    cur1.execute('INSERT INTO questions (question,theme, a, b, c) VALUES (?, ?, ?, ?, ?)',
                 [q1.core, 'math', q1.a, q1.b, q1.c])
    conn1.commit()
    cur1.execute('INSERT INTO questions (question,theme, a, b, c) VALUES (?, ?, ?, ?, ?)',
                 ['3 + 3 * 3 ** 3= ', 'math', '84', '81', '5832'])
    conn1.commit()
    cur1.execute('INSERT INTO questions (question,theme, a, b, c) VALUES (?, ?, ?, ?, ?)',
                 ['сколько дней недели в апреле?', 'math', '30', '7', '31'])
    conn1.commit()
    cur1.execute('INSERT INTO questions (question,theme, a, b, c) VALUES (?, ?, ?, ?, ?)',
                 ['какие из нижеперечисленных высказываний НЕ относятся к гачи культуре:', 'mem', '300 bucks',
                  'COME ON lets go', 'Sorry, i am chicken'])
    conn1.commit()
    cur1.execute('INSERT INTO questions (question,theme, a, b, c) VALUES (?, ?, ?, ?, ?)',
                 ['на пенек сел...', 'mem', 'Потом встал', 'Касарь должен был отдать', 'Ну раз сел, так и сиди'])
    conn1.commit()
    cur1.execute('INSERT INTO questions (question,theme, a, b, c) VALUES (?, ?, ?, ?, ?)',
                 ['ну че, как там с деньгами?', 'mem', 'Внес в капитал прожиточного минимума.', 'С какими деньгами?!',
                  'Ты кому звонишь сопля?!'])
    conn1.commit()
    cur1.execute('INSERT INTO questions (question,theme, a, b, c) VALUES (?, ?, ?, ?, ?)',
                 ['мы ребята удалые - лазим в щели половые - ?', 'beasts', 'Строители разлившие бетон',
                  'Сёстры Вачовски', 'Тараканы'])
    conn1.commit()
    cur1.execute('INSERT INTO questions (question,theme, a, b, c) VALUES (?, ?, ?, ?, ?)',
                 ['Cобака - 3, кошка - 3, корова - 2, петух - 8, Д.А.Медведев - ?', 'beasts',
                  'Наша страна не раз проходила\n через серьёзные испытания:\n и печенеги её терзали, и половцы',
                  'Вы держитесь здесь, вам всего доброго,\n хорошего настроения и здоровья!', '5'])
    conn1.commit()
    cur1.execute('INSERT INTO questions (question,theme, a, b, c) VALUES (?, ?, ?, ?, ?)',
                 ['что появилось раньше, курица или яйцо?', 'beasts', 'Курица', 'Олды', 'Яйцо'])
    conn1.commit()

user_id = None
login, password, start_testings = None, None, None


def pass_sha256(user_pass):
    salt = 'hold_the_door'
    password = bytes(user_pass + salt, 'utf8')
    pass_hash = hashlib.sha256(password)
    return pass_hash.hexdigest()


def register():
    try:
        login = ent_login.get().strip()
        password = pass_sha256(ent_pass.get())
        cur.execute('INSERT INTO list_users (login, password) VALUES (?, ?)', [login, password])
        conn.commit()
        if len(login) < 1 or password == '4f66d65bc5ce809a4661dada408c2de54533d6b70396513a46a23ecfcea79a06':
            raise Exception
        mb.showinfo('Регистрация', 'Пользователь ' + login + ' Успешно зарегистрирован!')

    except sqlite3.IntegrityError:
        mb.showerror('Ошибка ввода', 'Имя пользователя занято, выберите другое')
    except Exception:
        mb.showerror('Ошибка ввода', 'Поля должны быть заполнены')


def auth_window():
    def user_auth():
        global login, password
        login = ent_login_auth.get().strip()
        password = pass_sha256(ent_pass_auth.get())
        cur.execute('SELECT login FROM list_users WHERE login = ? AND password = ?', [login, password])
        info = cur.fetchone()
        if info:
            global start_testings
            start_testings = datetime.now()

            global user_id
            user_id = info[0]
            mb.showinfo('Авторизация', 'Добро пожаловать! - Доступ открыт!')
            mb.showinfo('Куда вы попали?', '''Вы участвуете в симуляции\n
            Собеседования в сферу АЙТИ\n
            Результат получите - после прохождения\n
            Всех испытаний. Приступайте прямо сейчас!''')

            root.destroy()
            conn.close()
        else:
            mb.showerror('Авторизация', 'Неверный логин или пароль')

    auth = Toplevel()
    auth.geometry('360x360')
    auth.title('Авторизация')
    auth.resizable(0, 0)

    lbl_main = Label(auth, text='Авторизация', font='calibri 20')
    lbl_main.place(x=20, y=20)

    lbl_login = Label(auth, text='Логин', font='calibri 14')
    lbl_login.place(x=20, y=100)

    ent_login_auth = Entry(auth, width=14, font='calibri 14')
    ent_login_auth.place(x=80, y=100)

    lbl_pass = Label(auth, text='Пароль', font='14')
    lbl_pass.place(x=20, y=160)

    ent_pass_auth = Entry(auth, width=14, font='calibri 14')
    ent_pass_auth.place(x=80, y=160)

    btn_auth = Button(auth, text='Войти', font='calibri 16', command=user_auth)
    btn_auth.place(x=20, y=200)


root = Tk()
root.geometry('500x500')
root.title('Главное меню')
root.resizable(0, 0)

lbl_main = Label(text='Регистрация', font='calibri 20')
lbl_main.place(x=20, y=20)

lbl_login = Label(text='Логин', font='calibri 14')
lbl_login.place(x=20, y=100)

ent_login = Entry(width=14, font='calibri 14')
ent_login.place(x=80, y=100)

lbl_pass = Label(text='Пароль', font='calibri 14')
lbl_pass.place(x=16, y=160)

ent_pass = Entry(width=14, font='calibri 14')
ent_pass.place(x=80, y=160)

btn_register = Button(text='Зарегистрироваться', font='calibri 16', command=register)
btn_register.place(x=20, y=200)

btn_auth = Button(text='Войти', font='calibri 16', command=auth_window)
btn_auth.place(x=20, y=270)

root.mainloop()
conn_t1 = sqlite3.connect('questions_new_data.db')
cur_t1 = conn_t1.cursor()
cur_t1.execute('SELECT COUNT(id) FROM questions')

len_id = int(cur_t1.fetchone()[0])
score_t1 = 0
score_t2 = 0
score_t3 = 0
list_res_t3 = []


def disable_this(button):
    button.configure(state=DISABLED)


def info_after_t1():
    mb.showinfo('Информация о кнопке справа',
                'Вы можете улучшить Ваш результат в тесте №1 добавив свой вариант вопроса')


def add_q_t1():
    '''функция добавляющая вопросы пользователя в тест на смекалку'''
    conn_t1_add_q = sqlite3.connect('questions_new_data.db')
    cur_t1_add_q = conn_t1_add_q.cursor()
    conn_t1_add_a = sqlite3.connect('answers_new_data.db')
    cur_t1_add_a = conn_t1_add_a.cursor()
    add_question_t1 = Toplevel()
    add_question_t1.geometry('1200x600')
    add_question_t1.title('Ваш вопрос')
    add_question_t1.resizable(0, 0)

    lbl_add_q = Label(add_question_t1, text='Текст вопроса (не более 120 символов)', font='calibri 16')
    lbl_add_q.place(x=20, y=0)

    ent_add_q = Entry(add_question_t1, width=120, font='calibri 12')
    ent_add_q.place(x=0, y=50)

    lbl_add_answ_a = Label(add_question_t1, text='Текст ответа a (не более 43 символов)', font='calibri 16')
    lbl_add_answ_a.place(x=20, y=100)
    ent_add_answ_a = Entry(add_question_t1, width=43, font='calibri 12')
    ent_add_answ_a.place(x=0, y=150)

    lbl_add_answ_b = Label(add_question_t1, text='Текст ответа b (не более 43 символов)', font='calibri 16')
    lbl_add_answ_b.place(x=20, y=200)
    ent_add_answ_b = Entry(add_question_t1, width=43, font='calibri 12')
    ent_add_answ_b.place(x=0, y=250)

    lbl_add_answ_c = Label(add_question_t1, text='Текст ответа c (не более 43 символов)', font='calibri 16')
    lbl_add_answ_c.place(x=20, y=300)
    ent_add_answ_c = Entry(add_question_t1, width=43, font='calibri 12')
    ent_add_answ_c.place(x=0, y=350)

    lbl_add_answ_true = Label(add_question_t1, text='Правильный вариант ответа\n (маленькая латинская буква a b или c)',
                              font='calibri 16')
    lbl_add_answ_true.place(x=500, y=150)
    ent_add_answ_true = Entry(add_question_t1, width=1, font='calibri 60')
    ent_add_answ_true.place(x=600, y=300)

    def check_fields():
        '''функция проверяет наличие ввода вопроса и ответа и добавляет данные в базы'''
        all_words_fields = [ent_add_q.get().strip(), ent_add_answ_a.get().strip(), ent_add_answ_b.get().strip(),
                            ent_add_answ_c.get().strip(), ent_add_answ_true.get()]
        while True:
            try:
                if all(map(lambda x: len(str(x)) > 0, all_words_fields)):
                    if ent_add_answ_true.get() in 'abc':
                        cur_t1_add_q.execute('INSERT INTO questions (question,theme, a, b, c) VALUES (?, ?, ?, ?, ?)',
                                             [all_words_fields[0], 'custom', all_words_fields[1], all_words_fields[2],
                                              all_words_fields[3]])
                        conn_t1_add_q.commit()
                        cur_t1_add_a.execute('INSERT INTO answers (answer) VALUES (?)', [all_words_fields[4]])
                        conn_t1_add_a.commit()
                        global score_t1, len_id
                        score_t1 += 1
                        len_id += 1
                        result_t1 = Button(text=f'Тест 1 {score_t1}/{len_id}', command=info_after_t1)
                        result_t1.place(x=0, y=0, anchor='nw', width=100, height=50)
                        mb.showinfo('Спасибо', 'Вы будете получать по 1 баллу за каждый предоставленный вопрос!')
                        choice_add = mb.askyesno('Тяжелый выбор', 'Хотите добавить еще вопрос?')
                        if choice_add:
                            add_question_t1.destroy()
                            add_q_t1()
                        add_question_t1.destroy()
                        disable_this(add_qt1)
                        conn_t1.close()
                        break
                    else:
                        raise ValueError
                else:
                    raise TypeError
            except ValueError:
                mb.showerror('Ошибка ответа',
                             'Выберите в качестве ответа маленькую латинскую букву a, b или c')
                break
            except TypeError:
                mb.showerror('Ошибка ввода',
                             'Все поля должны быть заполнены')
                break

    button_check = Button(add_question_t1, text=f'Проверить поля', command=check_fields)
    button_check.place(x=600, y=600, anchor='s', width=400, height=200)


def test1(number_q=1):
    '''тест на смекалку'''
    conn_t1 = sqlite3.connect('questions_new_data.db')
    cur_t1 = conn_t1.cursor()
    cur_t1.execute('SELECT COUNT(id) FROM questions')

    disable_this(open_button)
    len_id = int(cur_t1.fetchone()[0])
    test_1 = Toplevel()
    test_1.geometry('1200x600')
    test_1.title('Проверка Смекалки')
    test_1.resizable(0, 0)
    cur_t1.execute(f'SELECT question,theme, a, b, c FROM questions WHERE id = {number_q} ')
    answ_date = cur_t1.fetchall()

    def next_q():
        '''переход на следующий вопрос'''
        if number_q < len_id:
            test1(number_q + 1)
        else:
            mb.showinfo('Тест завершён', f'Ваш результат {score_t1} правильных ответов из {len_id}')
            result_t1 = Button(text=f'Тест 1 {score_t1}/{len_id}', command=info_after_t1)
            result_t1.place(x=0, y=0, anchor='nw', width=100, height=50)
            global add_qt1
            add_qt1 = Button(text=f'Добавить свой вопрос', command=add_q_t1)
            add_qt1.place(x=100, y=0, anchor='nw', width=200, height=50)
            check_end_tests()

    def checking_a():
        conn_t1_a = sqlite3.connect('answers_new_data.db')
        cur_t1_a = conn_t1_a.cursor()
        cur_t1_a.execute(f'SELECT answer FROM answers WHERE  id = ? AND answer = ?', [number_q, 'a'])
        cheeck = cur_t1_a.fetchone()
        if cheeck:
            global score_t1
            score_t1 += 1
            test_1.destroy()
            next_q()
        else:
            test_1.destroy()
            next_q()

    def checking_b():
        conn_t1_a = sqlite3.connect('answers_new_data.db')
        cur_t1_a = conn_t1_a.cursor()
        cur_t1_a.execute(f'SELECT answer FROM answers WHERE  id = ? AND answer = ?', [number_q, 'b'])
        cheeck = cur_t1_a.fetchone()
        if cheeck:
            global score_t1
            score_t1 += 1
            test_1.destroy()
            next_q()
        else:
            test_1.destroy()
            next_q()

    def checking_c():
        conn_t1_a = sqlite3.connect('answers_new_data.db')
        cur_t1_a = conn_t1_a.cursor()
        cur_t1_a.execute(f'SELECT answer FROM answers WHERE  id = ? AND answer = ?', [number_q, 'c'])
        cheeck = cur_t1_a.fetchone()
        if cheeck:
            global score_t1
            score_t1 += 1
            test_1.destroy()
            next_q()
        else:
            test_1.destroy()
            next_q()

    q_t1 = Label(test_1, text=f'''Вопрос №{number_q}: {answ_date[0][0]}''', font='calibri 14')
    q_t1.place(x=600, y=100, anchor='center')
    theme_t1 = Label(test_1, text=f'ТЕМА: {answ_date[0][1]}', font='calibri 20')
    theme_t1.place(x=600, y=50, anchor='center')
    a_t1 = Button(test_1, text=f'{answ_date[0][2]}', bg='red', activebackground='white', font='calibri 12',
                  command=checking_a)
    a_t1.place(x=200, y=600, anchor='s', width=400, height=200)
    b_t1 = Button(test_1, text=f'{answ_date[0][3]}', bg='green', activebackground='white', font='calibri 12',
                  command=checking_b)
    b_t1.place(x=600, y=600, anchor='s', width=400, height=200)
    c_t1 = Button(test_1, text=f'{answ_date[0][4]}', bg='blue', activebackground='white', font='calibri 12',
                  command=checking_c)
    c_t1.place(x=1000, y=600, anchor='s', width=390, height=200)


def launch():
    mb.showinfo('Подтверждено', 'Запуск ракеты по вашему приказу произведен!')
    disable_this(red_button)


def test2():
    '''тест на духовность'''
    mb.showinfo('Включите воображение', 'Представим, что вы отправились за священным граалем\nВсех джунов - '
                                        'придумайте сами, что это -\nВас просили включить воображение.'
                                        '\nВы долго искали и попали в священную пещеру,\nПосередине которой стоит алтарь.'
                                        '\nНа алтаре лежат предметы с интересными свойствами.\n\nКакой вы выберете?')

    def info_after_t2():
        mb.showinfo('Результат', 'Вашей аскезы')

    def very_bad_choice():
        mb.showinfo('Плохой выбор - тоже выбор...', 'Ваш выбор привел к полному затоплению священной пещеры\n'
                                                    'содержимым ближайшей сточной ямы')
        mb.showinfo('Итог', '0 баллов заслуженный результат.')
        result_t2 = Button(text=f'Тест 2 0/5', command=info_after_t2)
        result_t2.place(x=0, y=50, anchor='nw', width=100, height=50)
        disable_this(open_button1)
        test_2.destroy()
        check_end_tests()

    def bad_choice():
        mb.showinfo('Плохой выбор - тоже выбор...', 'Небеса разверзлись и поразили вас в самое сердце.\n'
                                                    'Но перед бесславной кончиной вы успели получить...')
        mb.showinfo('Итог', '1 балл заслуженный результат.')
        result_t2 = Button(text=f'Тест 2 1/5', command=info_after_t2)
        result_t2.place(x=0, y=50, anchor='nw', width=100, height=50)
        global score_t2
        score_t2 += 1
        disable_this(open_button1)
        test_2.destroy()
        check_end_tests()

    def good_choice():
        mb.showinfo('Интересный выбор', 'Вы на верном пути духовного просветления')
        mb.showinfo('Итог', '3 балла заслуженный результат.')
        result_t2 = Button(text=f'Тест 2 3/5', command=info_after_t2)
        result_t2.place(x=0, y=50, anchor='nw', width=100, height=50)
        global score_t2
        score_t2 += 3
        disable_this(open_button1)
        test_2.destroy()
        check_end_tests()

    def the_best_choice():
        mb.showinfo('В точку!', 'Снимаю шляпу и отдаю вам свой кнут, вы разгадали головоломку.')
        mb.showinfo('Итог', '5 - баллов лучший результат.')
        result_t2 = Button(text=f'Тест 2 5/5', command=info_after_t2)
        result_t2.place(x=0, y=50, anchor='nw', width=100, height=50)
        global score_t2
        score_t2 += 5
        disable_this(open_button1)
        test_2.destroy()
        check_end_tests()

    test_2 = Toplevel()
    test_2.geometry('1200x600')
    test_2.title('Проверка Духовности')
    test_2.resizable(0, 0)
    but_1 = Button(test_2, text='БАБЛОО!', bg='red', activebackground='black', font='calibri-bold 30',
                   command=very_bad_choice)
    but_1.place(relx=0.4, rely=0.3, width=300, height=300)
    but_2 = Button(test_2, text='Бугатти\n 100-метровая яхта\nквартира\nпрочие блага', bg='yellow',
                   activebackground='black', font='calibri 14', command=bad_choice)
    but_2.place(relx=0.0, rely=0.0, width=250, height=250)
    but_3 = Button(test_2, text='Здоровье\nBечная жизнь', bg='green', activebackground='black', font='calibri 24',
                   command=bad_choice)
    but_3.place(relx=0.8, rely=0.0, width=250, height=250)
    but_4 = Button(test_2, text='Суперспособность\nна выбор', bg='#03ffff', activebackground='black', font='calibri 20',
                   command=bad_choice)
    but_4.place(relx=0.01, rely=0.6, width=260, height=250)
    but_5 = Button(test_2, text='Всеобщая любовь\n и\nодобрение', bg='#ff03f7', activebackground='black',
                   font='calibri 20', command=bad_choice)
    but_5.place(relx=0.77, rely=0.67, width=260, height=240)
    but_6 = Button(test_2, text='Преисполниться\n в познании', bg='#0c695e', activebackground='#04a1d1',
                   font='calibri 16', command=good_choice)
    but_6.place(relx=0.225, rely=0.2, width=200, height=150)
    but_7 = Button(test_2, text='Стать Черным\nБаламутом', bg='#19078f', activebackground='#04a1d1', font='calibri 16',
                   command=good_choice)
    but_7.place(relx=0.68, rely=0.42, width=200, height=140)
    but_8 = Button(test_2, text='Путешествие в\nЧунга-чангу', bg='#81ad07', activebackground='#04a1d1',
                   font='calibri 16', command=good_choice)
    but_8.place(relx=0.24, rely=0.7, width=190, height=150)
    but_9 = Button(test_2, text='Простой\nдеревянный\nкубок', bg='#824522', activebackground='white', font='calibri 8',
                   command=the_best_choice)
    but_9.place(relx=0.7, rely=0.92, width=70, height=50)

    global red_button
    red_button = Button(text=f'Красная кнопка', bg='red', command=launch)
    red_button.place(x=100, y=50, anchor='nw', width=200, height=50)


def info_after_test3():
    mb.showinfo('Результат', 'Брюс Ли гордится Вами.')


def info_best_try():
    mb.showinfo('Задача: нажать все кнопки?', 'А Вы целеустремленный человек.')


def test3(attempts=2):
    '''тест на реакцию'''
    mb.showinfo('Проверка скорости реакции', 'Перед вами обыкновенная-волшебная печь\nИ кусок "волшебной-синей" глины\n'
                                             'Ваша задача:\nИспечь Колобок-кирпич и поймать его\n'
                                             'До того, как он успеет '
                                             '"сделать ноги"\nПосле нажатие на печь, ей понадобится\nНекоторое время '
                                             'на приготовление\nКогда Колобок-кирпич будет готов\n'
                                             'Нажмите на него - чтобы поймать')

    def catch_brick():
        '''бегуший кирпич'''
        global time_catch, list_res_t3, score_t3
        time_catch = time.perf_counter()
        res_catching = time_catch - time_start
        list_res_t3.append(res_catching)
        mb.showinfo('Результат охоты', f'Вы справились за {res_catching}')
        if res_catching < 0.8:
            score_t3 = 5
            mb.showinfo('очень быстро', 'Результат пилота F1')
        elif 1.3 > res_catching > 0.8:
            score_t3 = 3
            mb.showinfo('нормально', 'Под пиво - сойдет')
        elif 2 > res_catching > 1.3:
            score_t3 = 1
            mb.showinfo('медленно', 'Кто понял жизнь - тот не спешит')
        else:
            mb.showinfo('Поздравление', 'Скорее всего вы уже счастливый родитель-)')
            mb.showerror('В другой раз', 'Колобок-кирпич убежал')

        result_t3 = Button(text=f'Тест 3 {score_t3}/5', command=info_after_test3)
        result_t3.place(x=0, y=100, anchor='nw', width=100, height=50)

        best_try = Button(text=f'Лучший результат {round(min(list_res_t3), 3)} сек', command=info_best_try)
        best_try.place(x=100, y=100, anchor='nw', width=200, height=50)

        test_3.destroy()
        more_try = mb.askyesno('Улучшить результат', f'Можете поймать беглеца еще быстрее?\n'
                                                     f'количество попыток: {attempts}')
        if more_try:
            if attempts > 0:
                test3(attempts - 1)
            else:
                mb.showerror('Достаточно', 'Вы использовали все попытки')
                disable_this(open_button2)
                check_end_tests()
        else:
            disable_this(open_button2)
            check_end_tests()

    def start_kiln():
        '''затопить печь'''
        but_brick.destroy()
        time.sleep(randint(2, 11))
        global time_start
        time_start = time.perf_counter()
        but_brick1 = Button(test_3, text='КОЛОБИЧ', bg='#ad3b0a', activebackground='#d94404', font='calibri 10',
                            command=catch_brick)
        but_brick1.place(x=randint(0, 1150), y=randint(0, 750), width=80, height=40)

    test_3 = Toplevel()
    test_3.geometry('1200x800')
    test_3.title('Проверка реакции')
    test_3.resizable(0, 0)
    but_kiln = Button(test_3, text='Включить\nпечку', bg='#bd9482', activebackground='white', font='calibri-bold 40',
                      command=start_kiln)
    but_kiln.place(relx=0.4, rely=0.3, width=400, height=400)
    but_brick = Button(test_3, text='Синяя глина', bg='#b8a7a0', activebackground='black', font='calibri 9')
    but_brick.place(relx=0.4, rely=0.2, width=100, height=50)


def stats_try():
    '''добавление статистики в базу и переход к ее просмотру'''
    window.destroy()
    end_testings = datetime.now()
    score_res = score_t1 + score_t2 + score_t3
    percent_res = f'{(round((score_res / (10 + len_id)) * 100) - 1)}%'
    time_road = f'{end_testings - start_testings}'[:-6]
    cur_res.execute('SELECT COUNT(login) FROM results WHERE login = ?', [login])
    count_try_fetch = cur_res.fetchone()[0] + 1

    cur_res.execute('''INSERT INTO results (login, overall_result, percent_result, counter_try, date_start, date_end, time_test) 
    VALUES (?, ?, ?, ?, ?, ?, ?)''', [login, int(score_res), percent_res, str(count_try_fetch),
                                      str(start_testings)[:-6], str(end_testings)[:-6], time_road])
    con_res.commit()

    stats_window = Tk()
    stats_window.title("Результаты")
    stats_window.geometry('1200x600')
    stats_window.resizable(0, 0)

    prob_employment = Toplevel(stats_window)
    prob_employment.title("ПОЗДРАВЛЯЮ")
    prob_employment.geometry('1200x600')
    prob_employment.resizable(0, 0)

    last_lbl = Label(prob_employment, text='Вероятность вашего трудоустройства по результатам теста:',
                     font='calibri 20')
    last_lbl.place(anchor='center', x=600, y=100)
    last_lbl = Label(prob_employment, text=percent_res, font='calibri 120')
    last_lbl.place(anchor='center', x=600, y=300)

    def show_leaderboard():
        leaderboard = Toplevel()
        leaderboard.title("Лучшие попытки")
        leaderboard.geometry('1200x600')

        con_res = sqlite3.connect('results_new_data.db')
        cur_res = con_res.cursor()
        cur_res.execute('''SELECT  * FROM (SELECT  * FROM results   ORDER BY percent_result DESC)
        GROUP BY login ORDER BY percent_result DESC''')
        col = cur_res.fetchall()

        indexx = [i for i in range(len(col))]
        df_data = {'Login': [], 'score': [], 'correct_percent': [], 'date_start': [], 'date_end': [], 'time_road': []}
        for length_try in range(len(col)):
            df_data['Login'].append(col[length_try][1])
            df_data['score'].append(col[length_try][2])
            df_data['correct_percent'].append(col[length_try][3])
            df_data['date_start'].append(col[length_try][5])
            df_data['date_end'].append(col[length_try][6])
            df_data['time_road'].append(col[length_try][7])
        df = pd.DataFrame(df_data, index=indexx).head(10)
        pd.set_option('display.max_columns', None)

        lbl = Label(leaderboard, text=tabulate(df, headers='keys', tablefmt='presto'), font='calibri 16')
        lbl.grid(column=0, row=0)

    def show_all_try():
        leaderboard = Toplevel()
        leaderboard.title("Лучшие попытки")
        leaderboard.geometry('1200x600')
        con_res = sqlite3.connect('results_new_data.db')
        cur_res = con_res.cursor()
        cur_res.execute('SELECT  * FROM results WHERE login = ?', [login])
        col = cur_res.fetchall()

        indexx = [i for i in range(len(col))]
        df_data = {'Login': [], 'score': [], 'correct_percent': [], 'date_start': [], 'date_end': [], 'time_road': []}
        for length_try in range(len(col)):
            df_data['Login'].append(col[length_try][1])
            df_data['score'].append(col[length_try][2])
            df_data['correct_percent'].append(col[length_try][3])
            df_data['date_start'].append(col[length_try][5])
            df_data['date_end'].append(col[length_try][6])
            df_data['time_road'].append(col[length_try][7])
        df = pd.DataFrame(df_data, index=indexx).head(10)
        pd.set_option('display.max_columns', None)

        lbl = Label(leaderboard, text=tabulate(df, headers='keys', tablefmt='presto'), font='calibri 16')
        lbl.grid(column=0, row=0)

    def press_color():
        best_color = f'#{"".join([choice("0123456789ABCDEF") for _ in range(6)])}'
        colored_button = Button(text='Разноцветная\nКнопка', font='calibri 20', bg=best_color, command=press_color)
        colored_button.place(anchor='w', x=0, y=500, width=300, height=200)

    def road_to():
        stats_window.destroy()
        global open_button, open_button1, open_button2, window
        window = Tk()
        window.title('Роуд ту АйТи')
        window.geometry('800x600')
        nickname = Label(text=f'Пользователь {user_id}', font='calibri 40')
        nickname.place(x=400, y=300, anchor='center')
        open_button = Button(text='Смекалка', command=test1)
        open_button.place(x=500, y=500, anchor='se', width=100, height=50)
        open_button1 = Button(text='Духовность', command=test2)
        open_button1.place(x=400, y=500, anchor='se', width=100, height=50)
        open_button2 = Button(text='Реакция', command=test3)
        open_button2.place(x=300, y=500, anchor='se', width=100, height=50)
        window.mainloop()

    lead_button = Button(text='Таблица Лучших', font='calibri 20', command=show_leaderboard)
    lead_button.place(anchor='w', x=0, y=100, width=300, height=200)

    try_button = Button(text='Ваши попытки', font='calibri 20', command=show_all_try)
    try_button.place(anchor='w', x=0, y=300, width=300, height=200)

    colored_button = Button(text='Разноцветная\nКнопка', font='calibri 20', command=press_color)
    colored_button.place(anchor='w', x=0, y=500, width=300, height=200)

    restart_button = Button(text='Попробовать ЕЩЁ', font='calibri 60', bg='green', command=road_to)
    restart_button.place(anchor='w', x=300, y=300, width=900, height=600)

    quit_button = Button(text='СДАТЬСЯ', font='calibri 30', bg='red', command=quit)
    quit_button.place(x=300, y=500, width=900, height=100)

    stats_window.mainloop()


def check_end_tests():
    if all(map(lambda x: x['state'] == DISABLED, (open_button, open_button1, open_button2))):
        result = Button(text='Результат', command=stats_try)
        result.place(x=500, y=550, anchor='se', width=300, height=50)


if user_id:
    window = Tk()
    window.title('Роуд ту АйТи')
    window.geometry('800x600')
    nickname = Label(text=f'Пользователь {user_id}', font='calibri 40')
    nickname.place(x=400, y=300, anchor='center')
    open_button = Button(text='Смекалка', command=test1)
    open_button.place(x=500, y=500, anchor='se', width=100, height=50)
    open_button1 = Button(text='Духовность', command=test2)
    open_button1.place(x=400, y=500, anchor='se', width=100, height=50)
    open_button2 = Button(text='Реакция', command=test3)
    open_button2.place(x=300, y=500, anchor='se', width=100, height=50)
    window.mainloop()
