import time

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
    score = 0
    count_q = 1
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
    rerun = int(input('Еще партейку?\n1- ДА\n2- нет\n'))
    if rerun == 1:
        run()
    else:
        teleprint('cluck-cluck ' * 20)

try:
    run()
except:
    print('Используйте только цифры!')
    run()


