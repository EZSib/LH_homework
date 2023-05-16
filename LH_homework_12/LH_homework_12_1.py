from tkinter import *
from tkinter import messagebox as mb

root = Tk()
root.geometry('800x400')
root.title('Норма веса')
root.resizable(0, 0)


def weidth_calculate():
    try:
        height = int(ent_h.get())
        weidth = int(ent_w.get())
        choice = var.get()
        if choice == 0:
            raise KeyboardInterrupt
        elif choice == 1:
            best = height - 110
            mb.showinfo('Рассчёт готов!', f'Норма веса мужчины при росте {height} см равна {best} кг')
            if best > weidth:
                mb.showinfo('Результаты!', f'Исходя из Нормы веса вам надо набрать {best - weidth} кг')
            elif best < weidth:
                mb.showinfo('Результаты!', f'Исходя из Нормы веса вам надо сбросить {weidth - best} кг')
            else:
                mb.showinfo('Результаты!', f'ВЫ ИДЕАЛЬНЫ')
        elif choice == 2:
            best = height - 100
            mb.showinfo('Рассчёт готов!', f'Норма веса женщины при росте {height} см равна {best} кг')
            if best > weidth:
                mb.showinfo('Результаты!', f'Исходя из Нормы веса вам надо набрать {best - weidth} кг')
            elif best < weidth:
                mb.showinfo('Результаты!', f'Исходя из Нормы веса вам надо сбросить {weidth - best} кг')
            else:
                mb.showinfo('Результаты!', f'ВЫ ИДЕАЛЬНЫ')
    except TypeError:
        mb.showerror('Errrror!', 'Рост и вес должен быть целым числом!')
    except ValueError:
        mb.showerror('Errrror!', 'Поля должны быть заполнены!')
    except KeyboardInterrupt:
        mb.showerror('Errrror!', 'Выберите ваш пол!')
    ent_h.delete(0, 'end')
    ent_w.delete(0, 'end')


lbl_main = Label(text='Введите рост в сантиметрах и вес в килограммах', font='calibri 20')
lbl_main.place(x=20, y=20)

lbl_h = Label(text='Рост', font='calibri 14')
lbl_h.place(x=20, y=100)

ent_h = Entry(width=5, font='calibri 14')
ent_h.place(x=120, y=100)

lbl_w = Label(text='Вес', font='calibri 14')
lbl_w.place(x=20, y=160)

ent_w = Entry(width=5, font='calibri 14')
ent_w.place(x=120, y=160)

btn_calc = Button(text='Рассчитать', font='calibri 16', command=weidth_calculate)
btn_calc.place(x=20, y=200)

var = IntVar()

lbl_radio_button = Label(text='Ваш пол', font='calibri 14')
lbl_radio_button.place(x=250, y=100)

male = Radiobutton(text='мужской', variable=var, font='calibri 14', value=1)
male.place(x=200, y=150)

female = Radiobutton(text='женский', variable=var, font='calibri 14', value=2)
female.place(x=330, y=150)

root.mainloop()
