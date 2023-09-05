import sqlite3


def disable_this(button):
    button.configure(state=DISABLED)

def db_answ():
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

def db_quest():
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

def stats_try():
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

    prob_employment = Toplevel()
    prob_employment.title("ПОЗДРАВЛЯЮ")
    prob_employment.geometry('1200x600')
    prob_employment.resizable(0, 0)

    last_lbl = Label(prob_employment, text='Вероятность вашего трудоустройства по результатам теста:', font='calibri 20')
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


