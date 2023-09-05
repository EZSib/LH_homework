import hashlib
from datetime import datetime
import os
from func_db_q_db_a_result import *
from test1 import *
from test2 import *
from test3 import *

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
    db_answ()

if os.path.exists('questions_new_data.db'):
    pass
else:
    db_quest()

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
