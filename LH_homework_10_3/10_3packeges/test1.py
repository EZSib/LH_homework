import sqlite3

def disable_this(button):
    button.configure(state=DISABLED)
def info_after_t1():
    mb.showinfo('Информация о кнопке справа',
                'Вы можете улучшить Ваш результат в тесте №1 добавив свой вариант вопроса')


def add_q_t1():
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
