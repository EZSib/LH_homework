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
        if len(info) > 0:
            global user_id
            user_id = info[0]
            mb.showinfo('Авторизация', 'Добро пожаловать!')
            mb.showinfo('Доступ открыт', 'Доступ к прохождению тестов открыт!')


        else:
            mb.showerror('Авторизация', 'Неверный пароль')

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

if user_id:
    window = Tk()
    window.title('Тест №1')
    window.geometry('800x600')
    nickname = Label(text=user_id)
    open_button = Button(text='Тест 1')
    open_button.place(x=500, y=500, anchor='se', width=100, height=50)
    open_button1 = Button(text='Тест 2')
    open_button1.place(x=400, y=500, anchor='se', width=100, height=50)
    window.mainloop()