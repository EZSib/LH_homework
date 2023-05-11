# import sqlite3
# import hashlib
# import time
# from tkinter import *
# from tkinter import messagebox as mb

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
        else: quit()
    def checking_a():
        conn_t1_a = sqlite3.connect('answers_new_data.db')
        cur_t1_a = conn_t1_a.cursor()
        cur_t1_a.execute(f'SELECT answer FROM answers WHERE  id = ? AND answer = ?', [number_q, 'a'])
        cheeck = cur_t1_a.fetchone()
        if cheeck:
            global score_t1
            score_t1 += 1
            next_q()
        else:
            next_q()
    def checking_b():
        conn_t1_a = sqlite3.connect('answers_new_data.db')
        cur_t1_a = conn_t1_a.cursor()
        cur_t1_a.execute(f'SELECT answer FROM answers WHERE  id = ? AND answer = ?', [number_q, 'b'])
        cheeck = cur_t1_a.fetchone()
        if cheeck:
            global score_t1
            score_t1 += 1
            next_q()
        else:
            next_q()
    def checking_c():
        conn_t1_a = sqlite3.connect('answers_new_data.db')
        cur_t1_a = conn_t1_a.cursor()
        cur_t1_a.execute(f'SELECT answer FROM answers WHERE  id = ? AND answer = ?', [number_q, 'c'])
        cheeck = cur_t1_a.fetchone()
        if cheeck:
            global score_t1
            score_t1 += 1
            next_q()
        else:
            next_q()