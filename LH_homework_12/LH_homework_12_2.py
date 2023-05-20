from tkinter import *
from playsound import playsound
import winsound
from random import randint
import os

try:
    from playsound import playsound
except ImportError:
    os.system('pip install playsound')
    from playsound import playsound

root = Tk()
root.geometry('960x600')
root.title('Ксилофон')
root.resizable(0, 0)


def pik_pik():
    '''Воспроизведение 20 случайных звуков в промежутке от 50Гц до 5000Гц случайной продолжительностью 0.1-0.8 сек.'''
    for _ in range(20):
        winsound.Beep(randint(50, 5000), randint(100, 800))


def brother_play():
    '''Воспроизведение 15 нот в случайном порядке'''
    smpl_dct = {1: "playsound('noty-do.mp3')", 2: "playsound('re.mp3')", 3: "playsound('mi.mp3')",
                4: "playsound('fa.mp3')",
                5: "playsound('sol.mp3')", 6: "playsound('lja.mp3')", 7: "playsound('si.mp3')"}
    for _ in range(15):
        eval(smpl_dct[randint(1, 7)])


def info(event=None):
    creator_info = Toplevel(root)
    creator_info.title('Инфо о создателе')
    creator_info.geometry('960x600')
    creator_info.resizable(0, 0)
    rock_paint = Label(creator_info, text='Я Ксилофониатором командую!\nЕфим', font='calibri 40')
    rock_paint.pack(side=TOP)

def destr(event=None):
    root.destroy()



lbl_main = Label(text='На этом можно сыграть, не вызывая грузчиков', font='calibri 28')
lbl_main.pack(side=TOP)

lbl_minor = Label(text='Справка создателя F1', font='calibri 12')
lbl_minor.pack(side=TOP)

lbl_minor = Label(text='ДО-q     РЕ-w     МИ-e      ФА-r       СОЛЬ-t    ЛЯ -y      СИ-u', font='calibri 24')
lbl_minor.pack(side=TOP)

btn_do = Button(text='ДО', font='calibri 16', command=lambda: playsound('noty-do.mp3'), width=9, height=11)
btn_do.pack(side=LEFT)

btn_re = Button(text='РЕ', font='calibri 16', command=lambda: playsound('re.mp3'), width=9, height=11)
btn_re.pack(side=LEFT)

btn_mi = Button(text='МИ', font='calibri 16', command=lambda: playsound('mi.mp3'), width=9, height=11)
btn_mi.pack(side=LEFT)

btn_fa = Button(text='ФА', font='calibri 16', command=lambda: playsound('fa.mp3'), width=9, height=11)
btn_fa.pack(side=LEFT)

btn_sol = Button(text='СОЛЬ', font='calibri 16', command=lambda: playsound('sol.mp3'), width=9, height=11)
btn_sol.pack(side=LEFT)

btn_lja = Button(text='ЛЯ', font='calibri 16', command=lambda: playsound('lja.mp3'), width=9, height=11)
btn_lja.pack(side=LEFT)

btn_si = Button(text='СИ', font='calibri 16', command=lambda: playsound('si.mp3'), width=10, height=11)
btn_si.pack(side=LEFT)

btn_1 = Button(text='БА', font='calibri 16', bg='grey', command=lambda: winsound.Beep(2500, 500))
btn_1.place(x=0, y=525, width=100, height=75)
btn_2 = Button(text='ДА', font='calibri 16', bg='red', command=lambda: winsound.Beep(2000, 500))
btn_2.place(x=100, y=525, width=100, height=75)
btn_3 = Button(text='БУ', font='calibri 16', bg='green', command=lambda: winsound.Beep(1500, 500))
btn_3.place(x=200, y=525, width=100, height=75)
btn_4 = Button(text='М', font='calibri 16', bg='blue', command=lambda: winsound.Beep(1000, 500))
btn_4.place(x=300, y=525, width=100, height=75)
btn_5 = Button(text='С', font='calibri 16', bg='purple', command=lambda: winsound.Beep(500, 500))
btn_5.place(x=400, y=525, width=100, height=75)

bad_sound = Button(text='Издать звуки', font='calibri 16', bg='black', fg='yellow', command=pik_pik)
bad_sound.place(x=500, y=525, width=230, height=75)

good_sound = Button(text='Пьяные грузчики\nПоднимают на 10 этаж', font='calibri 12', bg='black', fg='yellow',
                    command=brother_play)
good_sound.place(x=730, y=525, width=250, height=75)

root.bind('q', lambda event=None: playsound('noty-do.mp3'))
root.bind('w', lambda event=None: playsound('re.mp3'))
root.bind('e', lambda event=None: playsound('mi.mp3'))
root.bind('r', lambda event=None: playsound('fa.mp3'))
root.bind('t', lambda event=None: playsound('sol.mp3'))
root.bind('y', lambda event=None: playsound('lja.mp3'))
root.bind('u', lambda event=None: playsound('si.mp3'))

root.bind('<F1>', info)
root.bind('<Escape>', destr)

root.mainloop()
