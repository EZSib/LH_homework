import sqlite3
import hashlib
from tkinter import *
from tkinter import messagebox as mb


# class Window(Tk):
#     def __init__(self):
#         super().__init__()
#
#         # конфигурация окна
#         self.title('Новое окно')
#         self.geometry('250x200')
#
#         # определение кнопки
#         self.button = Button(self, text='закрыть')
#         self.button['command'] = self.button_clicked
#         self.button.pack(anchor='center', expand=1)
#
#     def button_clicked(self):
#         self.destroy()






conn = sqlite3.connect('users_new_data.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS list_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login VARCHAR(64) NOT NULL UNIQUE,
    password VARCHAR(64) NOT NULL)''')

user_id = None

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
        mb.showinfo('Регистрация', 'Пользователь ' + login + ' Успешно зарегестрирован!')

    except sqlite3.IntegrityError:
        mb.showerror('Ошибка ввода', 'Имя пользователя занято, выберите другое')
    except Exception :
        mb.showerror('Ошибка ввода', 'Поля должны быть заполнены')


def auth_window():
    def user_auth():
        login = ent_login_auth.get().strip()
        password = pass_sha256(ent_pass_auth.get())
        cur.execute('SELECT login FROM list_users WHERE login = ? AND password = ?', [login, password])
        info = cur.fetchone()
        if info:
            global user_id
            user_id = info[0]
            mb.showinfo('Авторизация', 'Добро пожаловать!')
            mb.showinfo('Доступ открыт', 'Доступ к прохождению тестов открыт!')
            root.destroy()
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


def info_after_t1():
    mb.showinfo('Вы можете улучшить Ваш результат в тесте №1 добавив свой вариант вопроса')

def add_q_t1():
    pass

score_t1 = 0
def test1(number_q = 1):
    conn_t1 = sqlite3.connect('questions_new_data.db')
    cur_t1 = conn_t1.cursor()
    cur_t1.execute('SELECT COUNT(id) FROM questions')
    len_id = int(cur_t1.fetchone()[0])
    test_1 = Toplevel()
    test_1.geometry('1200x600')
    test_1.title('Тест1')
    test_1.resizable(0, 0)
    cur_t1.execute(f'SELECT question,theme, a, b, c FROM questions WHERE id = {number_q} ')
    answ_date = cur_t1.fetchall()


    def next_q():
        if number_q < len_id:
            test1(number_q + 1)
        else:
            mb.showinfo('Тест завершён', f'Ваш результат {score_t1} правильных ответов из {len_id}')
            result_t1 = Button(text=f'Тест 1 {score_t1}/{len_id}', command=info_after_t1)
            result_t1.place(x=0, y=0, anchor='nw', width=100, height=50)
            add_qt1 = Button(text=f'Добавить свой вопрос')
            add_qt1.place(x=100, y=0, anchor='nw', width=200, height=50)
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


    q_t1 = Label(test_1, text=f'''Вопрос № {number_q}
{answ_date[0][0]}''', font='calibri 14')
    q_t1.place(x=600, y=100, anchor='center')
    a_t1 = Button(test_1, text=f'{answ_date[0][2]}', bg='red', activebackground='white', font='calibri 12', command=checking_a)
    a_t1.place(x=200, y=600, anchor='s', width=400, height=200)
    b_t1 = Button(test_1, text=f'{answ_date[0][3]}', bg='green', activebackground='white', font='calibri 12', command=checking_b)
    b_t1.place(x=600, y=600, anchor='s', width=400, height=200)
    c_t1 = Button(test_1, text=f'{answ_date[0][4]}', bg='blue', activebackground='white', font='calibri 12', command=checking_c)
    c_t1.place(x=1000, y=600, anchor='s', width=390, height=200)







if user_id:
    window = Tk()
    window.title('Тест №1')
    window.geometry('800x600')
    nickname = Label(text=f'Пользователь {user_id}', font='calibri 26')
    nickname.place(x=300, y=300, anchor='center')
    open_button = Button(text='Тест 1', command=test1)
    open_button.place(x=500, y=500, anchor='se', width=100, height=50)
    open_button1 = Button(text='Тест 2')
    open_button1.place(x=400, y=500, anchor='se', width=100, height=50)



    window.mainloop()