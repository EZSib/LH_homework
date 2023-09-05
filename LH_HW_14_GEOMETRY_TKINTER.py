from tkinter import *
from tkinter import messagebox as mb
from math import pi
import os
from datetime import datetime
import webbrowser

'''1. Написать графическое приложение (tkinter) , где происходит расчет геометрических формул (нахождение площади прямоугольника, площади круга,
 площади треугольника).
2. Добавить в программу из первого задания расчет периметра прямоугольника, периметра круга и периметра треугольника с использованием lambda функций.
3. ** Вывести полученные результаты в файл result.txt и открыть его через текстовый редактор по нажатии кнопки "Расчитать".'''

del_ent = ["ent_side1.delete(0, 'end')",
           "ent_side2.delete(0, 'end')",
           "ent_side3.delete(0, 'end')",
           "ent_a.delete(0, 'end')",
           "ent_r.delete(0, 'end')",
           "ent_h.delete(0, 'end')"]
if not os.path.exists('result.txt'):
    with open('result.txt', 'w', encoding='utf8'):
        pass


def prnt_res():
    with open('result.txt', 'a', encoding='utf8') as f:
        print(text, file=f)
    [eval(i) for i in del_ent]
    webbrowser.open('result.txt')

def help_s_rec():
    try:
        global res, text
        f = lambda a, b: a * b
        res = f(int(ent_side1.get().strip()), int(ent_side3.get().strip()))
        res_calc.set(f'Результат: {res}')
        text = f'{datetime.now()} Площадь прямоугольника со сторонами {ent_side1.get().strip()} и {ent_side3.get().strip()} = {res}'
        btn_w_res = Button(text='Записать', font=main_font, command=prnt_res)
        btn_w_res.place(x=200, y=300)


    except Exception as er:
        print(er)
        [eval(i) for i in del_ent]
        mb.showinfo('help',
                    'Для рассчёта площади прямоугольника введите значения в поля:сторона 1,сторона 3')


def help_p_cir():
    try:
        global res, text
        f = lambda r: round(2 * pi * r, 2)
        res_calc.set(f'Результат: {f(int(ent_r.get().strip()))}')
        res = f(int(ent_r.get().strip()))
        text = f'{datetime.now()} Периметра круга с радиусом {ent_r.get().strip()} = {res}'
        btn_w_res = Button(text='Записать', font=main_font, command=prnt_res)
        btn_w_res.place(x=200, y=300)
    except  Exception as er:
        print(er)
        [eval(i) for i in del_ent]
        mb.showinfo('help', 'Для рассчёта периметра круга введите значение в поле:радиус')


def help_p_rec():
    try:
        global res, text
        f = lambda a, b: (a + b) * 2
        res_calc.set(f'Результат: {f(int(ent_side1.get().strip()), (int(ent_side2.get().strip())))}')
        res = f(int(ent_side1.get().strip()), (int(ent_side2.get().strip())))
        text = f'{datetime.now()} Периметр прямоугольника со сторонами {ent_side1.get().strip()} и {ent_side2.get().strip()} = {res}'
        btn_w_res = Button(text='Записать', font=main_font, command=prnt_res)
        btn_w_res.place(x=200, y=300)
    except Exception as er:
        print(er)
        [eval(i) for i in del_ent]
        mb.showinfo('help', 'Для рассчёта периметра прямоугольника введите значения в поля:сторона 1,сторона 2')


def help_s_trg():
    try:
        global res, text
        f = lambda a, h: a * h * 0.5
        res_calc.set(f'Результат: {f(int(ent_a.get().strip()), (int(ent_h.get().strip())))}')
        res = f(int(ent_a.get().strip()), (int(ent_h.get().strip())))
        text = f'{datetime.now()} Площадь треугольника с основание {ent_a.get().strip()} и высотой {ent_h.get().strip()} = {res}'
        btn_w_res = Button(text='Записать', font=main_font, command=prnt_res)
        btn_w_res.place(x=200, y=300)
    except Exception as er:
        print(er)
        mb.showinfo('help', 'Для рассчёта площади треугольника введите значения в поля:основание, высота')
        [eval(i) for i in del_ent]


def help_s_cir():
    try:
        global res, text
        f = lambda  r: round(pi * r ** 2, 2)
        res_calc.set(f'Результат: {f(int(ent_r.get().strip()))}')
        res = f(int(ent_r.get().strip()))
        text = f'{datetime.now()} Площадь круга с радиусом {ent_r.get().strip()} = {res}'
        btn_w_res = Button(text='Записать', font=main_font, command=prnt_res)
        btn_w_res.place(x=200, y=300)
    except Exception as er:
        print(er)
        mb.showinfo('help', 'Для рассчёта площади круга введите значение в поле:радиус')
        [eval(i) for i in del_ent]


def help_p_trg():
    try:
        global res, text
        f = lambda a, b, c: a + b + c
        res_calc.set(
            f'Результат: {f(int(ent_side1.get().strip()), int(ent_side2.get().strip()), int(ent_side3.get().strip()))}')
        res = f(int(ent_side1.get().strip()), int(ent_side2.get().strip()), int(ent_side3.get().strip()))
        text = f'{datetime.now()} Площадь треугольника со сторонами {ent_side1.get().strip()}, {ent_side2.get().strip()} и {ent_side3.get().strip()} = {res}'
        btn_w_res = Button(text='Записать', font=main_font, command=prnt_res)
        btn_w_res.place(x=200, y=300)
    except Exception as er:
        print(er)
        mb.showinfo('help',
                    'Для рассчёта периметра треугольника введите значения в поля:сторона 1,сторона 2, сторона 3')
        [eval(i) for i in del_ent]


root = Tk()
root.geometry('500x500')
root.title('Расчет геометрических формул')
root.resizable(0, 0)

main_font = 'calibri 14'
lbl_side1 = Label(text='сторона 1', font=main_font)
lbl_side1.place(x=20, y=60)

lbl_side2 = Label(text='сторона 2', font=main_font)
lbl_side2.place(x=20, y=100)

lbl_side3 = Label(text='сторона 3', font=main_font)
lbl_side3.place(x=20, y=140)

lbl_h = Label(text='высота', font=main_font)
lbl_h.place(x=20, y=180)

lbl_r = Label(text='радиус', font=main_font)
lbl_r.place(x=20, y=220)

lbl_a = Label(text='основание', font=main_font)
lbl_a.place(x=20, y=260)

lbl_a = Label(text='Как рассчитать', font=main_font)
lbl_a.place(x=150, y=15)

res_calc = StringVar()
lbl_res = Label(textvariable=res_calc, font=main_font)
lbl_res.place(x=20, y=300)

ent_side1 = Entry(width=5, font=main_font)
ent_side1.place(x=120, y=60)

ent_side2 = Entry(width=5, font=main_font)
ent_side2.place(x=120, y=100)

ent_side3 = Entry(width=5, font=main_font)
ent_side3.place(x=120, y=140)

ent_h = Entry(width=5, font=main_font)
ent_h.place(x=120, y=180)

ent_r = Entry(width=5, font=main_font)
ent_r.place(x=120, y=220)

ent_a = Entry(width=5, font=main_font)
ent_a.place(x=120, y=260)

btn_srec = Button(text='S прямоугольника', font=main_font, command=help_s_rec)
btn_srec.place(x=200, y=55)

btn_scir = Button(text='S круга', font=main_font, command=help_s_cir)
btn_scir.place(x=200, y=95)

btn_stria = Button(text='S треугольника', font=main_font, command=help_s_trg)
btn_stria.place(x=200, y=135)

btn_prec = Button(text='P круга ', font=main_font, command=help_p_cir)
btn_prec.place(x=200, y=175)

btn_ptrec = Button(text='P прямоугольника', font=main_font, command=help_p_rec)
btn_ptrec.place(x=200, y=215)

btn_ptria = Button(text='P треугольника', font=main_font, command=help_p_trg)
btn_ptria.place(x=200, y=255)

root.mainloop()
