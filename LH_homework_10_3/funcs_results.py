import sqlite3
from tkinter import *
from tkinter import messagebox as mb
import time
from random import *
from datetime import datetime
import pandas as pd
from tabulate import tabulate

window = Tk()
window.title("Результаты")
window.geometry('1200x600')
login = 'йй'


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


lead_button = Button(text='Таблица Лучших', font='calibri 20', command=show_leaderboard)
lead_button.place(anchor='w', x=0, y=100, width=300, height=200)

try_button = Button(text='Ваши попытки', font='calibri 20', command=show_all_try)
try_button.place(anchor='w', x=0, y=300, width=300, height=200)

colored_button = Button(text='Разноцветная\nКнопка', font='calibri 20', command=press_color)
colored_button.place(anchor='w', x=0, y=500, width=300, height=200)

restart_button = Button(text='Попробовать ЕЩЁ', font='calibri 60', bg='green')
restart_button.place(anchor='w', x=300, y=300, width=900, height=600)

quit_button = Button(text='СДАТЬСЯ', font='calibri 30', bg='red', command=quit)
quit_button.place(x=300, y=500, width=900, height=100)

window.mainloop()
