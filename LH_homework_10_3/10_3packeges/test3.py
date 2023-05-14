from tkinter import *
from tkinter import messagebox as mb
import time
def disable_this(button):
    button.configure(state=DISABLED)
def info_after_test3():
    mb.showinfo('Результат', 'Брюс Ли гордится Вами.')


def info_best_try():
    mb.showinfo('Задача: нажать все кнопки?', 'А Вы целеустремленный человек.')


def test3(attempts=2):
    mb.showinfo('Проверка скорости реакции', 'Перед вами обыкновенная-волшебная печь\nИ кусок "волшебной-синей" глины\n'
                                             'Ваша задача:\nИспечь Колобок-кирпич и поймать его\n'
                                             'До того, как он успеет '
                                             '"сделать ноги"\nПосле нажатие на печь, ей понадобится\nНекоторое время '
                                             'на приготовление\nКогда Колобок-кирпич будет готов\n'
                                             'Нажмите на него - чтобы поймать')

    def catch_brick():
        global time_catch, list_res_t3, score_t3
        time_catch = time.perf_counter()
        res_catching = time_catch - time_start
        list_res_t3.append(res_catching)
        mb.showinfo('Результат охоты', f'Вы справились за {res_catching}')
        if res_catching < 0.8:
            score_t3 = 5
            mb.showinfo('очень быстро', 'Результат пилота F1')
        elif 1.3 > res_catching > 0.8:
            score_t3 = 3
            mb.showinfo('нормально', 'Под пиво - сойдет')
        elif 2 > res_catching > 1.3:
            score_t3 = 1
            mb.showinfo('медленно', 'Кто понял жизнь - тот не спешит')
        else:
            mb.showinfo('Поздравление', 'Скорее всего вы уже счастливый родитель-)')
            mb.showerror('В другой раз', 'Колобок-кирпич убежал')

        result_t3 = Button(text=f'Тест 3 {score_t3}/5', command=info_after_test3)
        result_t3.place(x=0, y=100, anchor='nw', width=100, height=50)

        best_try = Button(text=f'Лучший результат {round(min(list_res_t3), 3)} сек', command=info_best_try)
        best_try.place(x=100, y=100, anchor='nw', width=200, height=50)

        test_3.destroy()
        more_try = mb.askyesno('Улучшить результат', f'Можете поймать беглеца еще быстрее?\n'
                                                     f'количество попыток: {attempts}')
        if more_try:
            if attempts > 0:
                test3(attempts - 1)
            else:
                mb.showerror('Достаточно', 'Вы использовали все попытки')
                disable_this(open_button2)
                check_end_tests()
        else:
            disable_this(open_button2)
            check_end_tests()

    def start_kiln():
        but_brick.destroy()
        time.sleep(randint(2, 11))
        global time_start
        time_start = time.perf_counter()
        but_brick1 = Button(test_3, text='КОЛОБИЧ', bg='#ad3b0a', activebackground='#d94404', font='calibri 10',
                            command=catch_brick)
        but_brick1.place(x=randint(0, 1150), y=randint(0, 750), width=80, height=40)

    test_3 = Toplevel()
    test_3.geometry('1200x800')
    test_3.title('Проверка реакции')
    test_3.resizable(0, 0)
    but_kiln = Button(test_3, text='Включить\nпечку', bg='#bd9482', activebackground='white', font='calibri-bold 40',
                      command=start_kiln)
    but_kiln.place(relx=0.4, rely=0.3, width=400, height=400)
    but_brick = Button(test_3, text='Синяя глина', bg='#b8a7a0', activebackground='black', font='calibri 9')
    but_brick.place(relx=0.4, rely=0.2, width=100, height=50)
