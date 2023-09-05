from tkinter import *
from tkinter import messagebox as mb

def disable_this(button):
    button.configure(state=DISABLED)
def launch():
    mb.showinfo('Подтверждено', 'Запуск ракеты по вашему приказу произведен!')
    disable_this(red_button)


def test2():
    mb.showinfo('Включите воображение', 'Представим, что вы отправились за священным граалем\nВсех джунов - '
                                        'придумайте сами, что это -\nВас просили включить воображение.'
                                        '\nВы долго искали и попали в священную пещеру,\nПосередине которой стоит алтарь.'
                                        '\nНа алтаре лежат предметы с интересными свойствами.\n\nКакой вы выберете?')

    def info_after_t2():
        mb.showinfo('Результат', 'Вашей аскезы')

    def very_bad_choice():
        mb.showinfo('Плохой выбор - тоже выбор...', 'Ваш выбор привел к полному затоплению священной пещеры\n'
                                                    'содержимым ближайшей сточной ямы')
        mb.showinfo('Итог', '0 баллов заслуженный результат.')
        result_t2 = Button(text=f'Тест 2 0/5', command=info_after_t2)
        result_t2.place(x=0, y=50, anchor='nw', width=100, height=50)
        disable_this(open_button1)
        test_2.destroy()
        check_end_tests()

    def bad_choice():
        mb.showinfo('Плохой выбор - тоже выбор...', 'Небеса разверзлись и поразили вас в самое сердце.\n'
                                                    'Но перед бесславной кончиной вы успели получить...')
        mb.showinfo('Итог', '1 балл заслуженный результат.')
        result_t2 = Button(text=f'Тест 2 1/5', command=info_after_t2)
        result_t2.place(x=0, y=50, anchor='nw', width=100, height=50)
        global score_t2
        score_t2 += 1
        disable_this(open_button1)
        test_2.destroy()
        check_end_tests()

    def good_choice():
        mb.showinfo('Интересный выбор', 'Вы на верном пути духовного просветления')
        mb.showinfo('Итог', '3 балла заслуженный результат.')
        result_t2 = Button(text=f'Тест 2 3/5', command=info_after_t2)
        result_t2.place(x=0, y=50, anchor='nw', width=100, height=50)
        global score_t2
        score_t2 += 3
        disable_this(open_button1)
        test_2.destroy()
        check_end_tests()

    def the_best_choice():
        mb.showinfo('В точку!', 'Снимаю шляпу и отдаю вам свой кнут, вы разгадали головоломку.')
        mb.showinfo('Итог', '5 - баллов лучший результат.')
        result_t2 = Button(text=f'Тест 2 5/5', command=info_after_t2)
        result_t2.place(x=0, y=50, anchor='nw', width=100, height=50)
        global score_t2
        score_t2 += 5
        disable_this(open_button1)
        test_2.destroy()
        check_end_tests()

    test_2 = Toplevel()
    test_2.geometry('1200x600')
    test_2.title('Проверка Духовности')
    test_2.resizable(0, 0)
    but_1 = Button(test_2, text='БАБЛОО!', bg='red', activebackground='black', font='calibri-bold 30',
                   command=very_bad_choice)
    but_1.place(relx=0.4, rely=0.3, width=300, height=300)
    but_2 = Button(test_2, text='Бугатти\n 100-метровая яхта\nквартира\nпрочие блага', bg='yellow',
                   activebackground='black', font='calibri 14', command=bad_choice)
    but_2.place(relx=0.0, rely=0.0, width=250, height=250)
    but_3 = Button(test_2, text='Здоровье\nBечная жизнь', bg='green', activebackground='black', font='calibri 24',
                   command=bad_choice)
    but_3.place(relx=0.8, rely=0.0, width=250, height=250)
    but_4 = Button(test_2, text='Суперспособность\nна выбор', bg='#03ffff', activebackground='black', font='calibri 20',
                   command=bad_choice)
    but_4.place(relx=0.01, rely=0.6, width=260, height=250)
    but_5 = Button(test_2, text='Всеобщая любовь\n и\nодобрение', bg='#ff03f7', activebackground='black',
                   font='calibri 20', command=bad_choice)
    but_5.place(relx=0.77, rely=0.67, width=260, height=240)
    but_6 = Button(test_2, text='Преисполниться\n в познании', bg='#0c695e', activebackground='#04a1d1',
                   font='calibri 16', command=good_choice)
    but_6.place(relx=0.225, rely=0.2, width=200, height=150)
    but_7 = Button(test_2, text='Стать Черным\nБаламутом', bg='#19078f', activebackground='#04a1d1', font='calibri 16',
                   command=good_choice)
    but_7.place(relx=0.68, rely=0.42, width=200, height=140)
    but_8 = Button(test_2, text='Путешествие в\nЧунга-чангу', bg='#81ad07', activebackground='#04a1d1',
                   font='calibri 16', command=good_choice)
    but_8.place(relx=0.24, rely=0.7, width=190, height=150)
    but_9 = Button(test_2, text='Простой\nдеревянный\nкубок', bg='#824522', activebackground='white', font='calibri 8',
                   command=the_best_choice)
    but_9.place(relx=0.7, rely=0.92, width=70, height=50)

    global red_button
    red_button = Button(text=f'Красная кнопка', bg='red', command=launch)
    red_button.place(x=100, y=50, anchor='nw', width=200, height=50)
