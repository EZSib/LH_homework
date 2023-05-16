from tkinter import *
from tkinter import messagebox as mb
from random import *


root = Tk()
root.title("Игральная кость")
root.geometry('500x500')
root.resizable(0, 0)

def set_cube():
    btn_go['text'] = 'eschoraz!!!!!!!!'
    num = randint(1, 6)
    path = f'{num}.png'
    img['file'] = path

def set_cube_event(event):
    set_cube()

lbl_rules = Label(text='lol-kek-cheburek', font='calibri 14')
lbl_rules.pack(side=TOP)

lbl_main = Label(text='Игральная кость', font='calibri 20', justify=CENTER)
lbl_main.pack(side=TOP)

img = PhotoImage(file='1.png')

lbl_img = Label(image=img)
lbl_img.pack(side=TOP)

btn_go = Button(text='GOGOGOGO', command=set_cube)
btn_go.pack(side=TOP)

root.bind('<Return>', set_cube_event)

root.mainloop()