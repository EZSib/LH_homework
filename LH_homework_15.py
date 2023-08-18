'''1. Напишите две функции создания списка из четных чисел от 0 до N (N – аргумент функции):
[0, 2, 4, …, N] с помощью метода append и с помощью инструмента list comprehensions (генератор списков).
 Через декоратор определите время работы этих функций.
2. Вернитесь к задаче "Викторина" из первого урока . Через декоратор запишите информацию в базу данных.'''

# '====================================================================================================================='
from datetime import datetime
import sqlite3
import time

def time_dec(func):
    def action(x):
        now = datetime.now()
        func(x)
        return  datetime.now() - now
    return action
@time_dec
def func_even_append(n):
    list_even = []
    for i in range(0, n):
        if i % 2 ==0:
            list_even.append(i)
    return list_even
@time_dec
def func_even_comprehensions(n):
    return [i for i in range(0, n) if i % 2 ==0]

print(func_even_append(1000000))
print(func_even_comprehensions(1000000))
# '====================================================================================================================='

def sql3_insert(func):
    def action():
        func()
        conn = sqlite3.connect('results.db')
        cur = conn.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS list_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login VARCHAR(64) NOT NULL UNIQUE,
            result INTEGER (1) NOT NULL)''')

        cur.execute('INSERT INTO list_results (login, result) VALUES (?, ?)', [name, score])
        conn.commit()
        rerun = int(input('Еще партейку?\n1- ДА\n2- нет\n'))
        if rerun == 1:
            func()
        else:
            teleprint('cluck-cluck ' * 20)
    return action


data_math = [f' 2 + 2 * 2: \n1- 8\n2- 6\n3- 16\n',
             f'3 + 3 * 3 ** 3:\n1- 84\n2- 81\n3- 5832\n',
             f'сколько дней недели в апреле?\n1- 30\n2- 7\n3- 31\n']

data_mem = [
    ' какие из нижеперечисленных высказываний НЕ относятся к гачи культуре:\n1- 300 bucks\n2- COME ON lets go\n3- Sorry, i am chicken\n',
    'на пенек сел...\n1- Потом встал\n2- Касарь должен был отдать\n3- Ну раз сел, так и сиди\n',
    '''ну че, как там с деньгами?
    1- Это служба безопасности сбербанка,ваши средства в опасности, срочно переведите их на ... безопасный счет!
    2- С какими деньгами?! 
    3- Ты кому звонишь сопля?!\n''']

data_beasts = [
    ' мы ребята удалые - лазим в щели половые - ?\n1- Строители разлившие бетон\n2- Сёстры Вачовски\n3- Тараканы\n',
    '''Cобака - 3, кошка - 3, корова - 2, петух - 8, Д.А.Медведев - ?
    1- Наша страна не раз проходила через серьёзные испытания: и печенеги её терзали, и половцы
    2- Вы держитесь здесь, вам всего доброго, хорошего настроения и здоровья!
    3- 5\n''',
    'что появилось раньше, курица или яйцо?\n1- Курица\n2- Олды\n3- Яйцо\n']

d_math_a = {2: True, '1': True, 2.0: True}
d_mem_a = {3: True, '2': True, 1.0: True}
d_beasts_a = {3: True, '2': True, 2.0: True}


@sql3_insert
def run():
    '''Запускает викторину, передает в функцию выбранную тематику'''
    print('Дбр пжлвт в вктрн!', 'Вы в теме?', '\t1 - По математике',
          '\t2 - По мемам', '\t3 - По животным', sep='\n')
    choice = int(input())
    vict(('', data_math, data_mem, data_beasts)[choice], ('', d_math_a, d_mem_a, d_beasts_a)[choice])

def teleprint(*args, delay=0.05, str_join=' '):
    '''Вывод с задержкой, псевдодекоратор'''
    text = str_join.join(str(x) for x in args)
    n = len(text)
    for i, char in enumerate(text, 1):
        if i == n:
            char = f'{char}\n'
        print(char, end='')
        time.sleep(delay)

def vict(select_data, answers):
    '''Перебираем вопросы, начисляем очки за правильные ответы'''
    global name, score
    score = 0
    count_q = 12
    for question in select_data:
        if count_q == 1:
            score += answers.get(int(input(question)), False)
        elif count_q == 2:
            score += answers.get(input(question), False)
        else:
            score += answers.get(float(input(question)), False)
        count_q += 1
        time.sleep(0.5)
    name = input('Введите ваше имя: \n')
    print(f'Результаты ваших трудов {score} из 3')

try:
    run()
except Exception as exp:
    print(exp)
    print('Используйте только цифры!')
    run()
# ==================================================================================================================




