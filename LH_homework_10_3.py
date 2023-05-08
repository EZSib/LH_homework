import sqlite3
import hashlib
from tkinter import *
from tkinter import  messagebox as mb

from pip._internal.network import auth

conn = sqlite3.connect('users_new_data.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS list_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login VARCHAR(64) NOT NULL UNIQUE,
    password VARCHAR(64) NOT NULL)''')

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
        if login == None or password == '4f66d65bc5ce809a4661dada408c2de54533d6b70396513a46a23ecfcea79a06':
            raise sqlite3.IntegrityError
        mb.showinfo('Регистрация', 'Пользователь ' + login + ' Успешно зарегестрирован!')
    except sqlite3.IntegrityError:
        mb.showerror('Ошибка ввода', 'Поля должны быть заполнены')

def auth_window():
    def user_auth():
        login = ent_login_auth.get().strip()
        password = pass_sha256(ent_pass_auth.get())
        cur.execute('SELECT password FROM list_users WHERE login = ? AND password = ?', [login, password])
        info = cur.fetchall()
        if len(info) > 0:
            mb.showinfo('Avtorizaciya', 'Dobro pozhalovatb')
        else: mb.showerror('Avtorizaciya', 'Nevernii parolb')

    auth = Toplevel()
    auth.geometry('360x360')
    auth.title('Avtorizaciya')
    auth.resizable(0, 0)

    lbl_main = Label(auth, text='Avtorizaciya', font='calibri 20')
    lbl_main.place(x=20, y=20)

    lbl_login = Label(auth, text='Login', font='calibri 14')
    lbl_login.place(x=20, y=100)

    ent_login_auth = Entry(auth, width=14, font='calibri 14')
    ent_login_auth.place(x=80, y=100)

    lbl_pass = Label(auth, text='Parolb', font='14')
    lbl_pass.place(x=20, y=160)

    ent_pass_auth = Entry(auth, width=14, font='calibri 14')
    ent_pass_auth.place(x=80, y=160)

    btn_auth = Button(auth, text= 'Voiti', font='calibri 16', command=user_auth)
    btn_auth.place(x=20, y=200)

root = Tk()
root.geometry('360x360')
root.title('Registaciya')
root.resizable(0, 0)

lbl_main = Label(text='Registaciya', font='calibri 20')
lbl_main.place(x=20, y=20)

lbl_login = Label(text='Login', font='calibri 14')
lbl_login.place(x=20, y=100)

ent_login = Entry(width=14, font='calibri 14')
ent_login.place(x=80, y=100)

lbl_pass = Label(text='Pass', font='calibri 14')
lbl_pass.place(x=20, y=160)

ent_pass = Entry(width=14, font='calibri 14')
ent_pass.place(x=80, y=160)

btn_register = Button(text='Zaregitsya', font='calibri 16', command=register)
btn_register.place(x=20, y=200)

btn_auth = Button(text='Voiti', font='calibri 16', command=auth_window)
btn_auth.place(x=20, y=270)

root.mainloop()