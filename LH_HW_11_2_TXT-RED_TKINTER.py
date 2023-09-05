'''Модернизируйте приложение из предыдущей задачи.
Ввод текста в .txt файл должен происходить через графическое приложение tkinter.'''

import os
from tkinter import *
from tkinter import messagebox as mb


def unlock():
    btn_field.configure(state=ACTIVE)

def print_text():
    if not os.path.exists('log.txt'):
        with open('log.txt', 'w', encoding='utf8') as f:
            print('log.txt already exists')

    with open('log.txt', 'a', encoding='utf8') as date:
        text = f'{ent_field.get().strip()}'
        if text == 'off':
            btn_field.configure(state=DISABLED)
        if text =='quit':
            quit()
        if text != 'off' and text != 'quit' and text != '':
            print(text, file=date)
        ent_field.delete(0, 'end')

def read_text():
    try:
        if not os.path.exists('log.txt'):
            mb.showerror('Файл отсутствует', 'Записи еще не сделаны')
    except:
        pass
    def display_text():
        with open('log.txt', 'r', encoding='utf8') as f:
            return f.read()
    a = display_text()
    window_text = Toplevel()
    window_text.resizable(0, 0)
    all_text = Label(window_text, text=a, font='calibri 14')
    all_text.place(x=0, y=0)

def clear_text():
    with open('log.txt', 'w', encoding='utf8') as date:
        date.close()

def overwrite_all_text():
    with open('log.txt', 'w', encoding='utf8') as date:
        text = f'{ent_field.get().strip()}'
        if text == 'off':
            btn_field.configure(state=DISABLED)
        if text =='quit':
            quit()
        if text != 'off' and text != 'quit' and text != '':
            print(text, file=date)
        ent_field.delete(0, 'end')



text_editor = Tk()
text_editor.geometry('1200x300')
text_editor.title('Текстовый редактор')
text_editor.resizable(0, 0)


lbl_field = Label(text='Введите текст в поле,нажмите на кнопку "записать" (off-заблокировать, quit-выйти)',
                  font='calibri 20')
lbl_field.place(x=0, y=0)

ent_field = Entry(width=100, font='calibri 12')
ent_field.place(x=0, y=50)

btn_field = Button(text='Записать строку', bg='#33fc14',  command=print_text)
btn_field.place(x=0, y=95, anchor='w')

btn_read = Button(text='Читать записанное', bg='#9d06d4', command=read_text)
btn_read.place(x=0, y=130, anchor='w')

btn_unlock = Button(text='Разблокировать', bg='blue',  command=unlock)
btn_unlock.place(x=0, y=165, anchor='w')

overwrite_text = Button(text='Перезаписать текст', bg='yellow',  command=overwrite_all_text)
overwrite_text.place(x=0, y=200, anchor='w')

delete_text = Button(text='Удалить текст', bg='red',  command=clear_text)
delete_text.place(x=0, y=235, anchor='w')

text_editor.mainloop()

