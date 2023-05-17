from tkinter import *
from itertools import cycle
from random import randint
import os

def resizeImage(img, newWidth, newHeight):
    old_width = img.width()
    old_height = img.height()
    new_photo_image = PhotoImage(width=newWidth, height=newHeight)
    for x in range(newWidth):
        for y in range(newHeight):
            xOld = int(x*old_width/newWidth)
            yOld = int(y*old_height/newHeight)
            rgb = '#%02x%02x%02x' % img.get(xOld, yOld)
            new_photo_image.put(rgb, (x, y))
    return new_photo_image

def end_see():
    root.destroy()
def next_rave():
    global alpha, root
    alpha += 1
    root.destroy()
    galery = [i for i in os.listdir() if i.endswith('.png')]
    forward = cycle(galery)
    result_iter_galery = next(forward)
    for _ in range(alpha):
        result_iter_galery = next(forward)
    def resizeImage(img, newWidth, newHeight):
        old_width = img.width()
        old_height = img.height()
        new_photo_image = PhotoImage(width=newWidth, height=newHeight)
        for x in range(newWidth):
            for y in range(newHeight):
                xOld = int(x*old_width/newWidth)
                yOld = int(y*old_height/newHeight)
                rgb = '#%02x%02x%02x' % img.get(xOld, yOld)
                new_photo_image.put(rgb, (x, y))
        return new_photo_image

    def end_see():
        root.destroy()

    root = Tk()
    root.geometry('900x600')
    root.title('Галерея')
    root.resizable(0, 0)
    root.configure(background='black')
    myCanvas = Canvas(root, width=555, height=550)
    myCanvas.place(x=140, y=50)
    puppyImage = PhotoImage(file=result_iter_galery)
    puppyImage = resizeImage(puppyImage, 555, 550)
    myCanvas.create_image(50, 50, anchor=NW, image=puppyImage)
    start_btn = Button(text="Закончить просмотр",bg='black', fg='pink', font='calibri 30', command=end_see)
    start_btn.place(x=190, y=0, height=100, width=515)

    start_left = Button(text="НАЗАД", bg='black', fg='yellow', height=30, width=23, command=prev_rave)
    start_left.pack(side=LEFT)

    start_right = Button(text="ВПЕРЕД",bg='black', fg='yellow', height=30,width=24, command=next_rave)
    start_right.pack(side=RIGHT)

    root.mainloop()

def prev_rave():
    global alpha, root
    alpha += 1
    root.destroy()
    galery = [i for i in os.listdir() if i.endswith('.png')]
    forward = cycle(reversed(galery))
    result_iter_galery = next(forward)
    for _ in range(alpha):
        result_iter_galery = next(forward)


    def resizeImage(img, newWidth, newHeight):
        old_width = img.width()
        old_height = img.height()
        new_photo_image = PhotoImage(width=newWidth, height=newHeight)
        for x in range(newWidth):
            for y in range(newHeight):
                xOld = int(x * old_width / newWidth)
                yOld = int(y * old_height / newHeight)
                rgb = '#%02x%02x%02x' % img.get(xOld, yOld)
                new_photo_image.put(rgb, (x, y))
        return new_photo_image

    def end_see():
        root.destroy()

    root = Tk()
    root.geometry('900x600')
    root.title('Галерея')
    root.resizable(0, 0)
    root.configure(background='black')
    myCanvas = Canvas(root, width=555, height=550)
    myCanvas.place(x=140, y=50)
    puppyImage = PhotoImage(file=result_iter_galery)
    puppyImage = resizeImage(puppyImage, 555, 550)
    myCanvas.create_image(50, 50, anchor=NW, image=puppyImage)
    start_btn = Button(text="Закончить просмотр", bg='black', fg='pink', font='calibri 30', command=end_see)
    start_btn.place(x=190, y=0, height=100, width=515)

    start_left = Button(text="НАЗАД", bg='black', fg='yellow', height=30, width=23, command=prev_rave)
    start_left.pack(side=LEFT)

    start_right = Button(text="ВПЕРЕД", bg='black', fg='yellow', height=30, width=24, command=next_rave)
    start_right.pack(side=RIGHT)

    root.mainloop()


galery = [i for i in os.listdir() if  i.endswith('.png') ]
alpha = randint(0,len(galery)-1)
root = Tk()
root.geometry('900x600')
root.title('Галерея')
root.resizable(0, 0)
root.configure(background='black')
myCanvas = Canvas(root, width=555, height=550)
myCanvas.place(x=140, y=50)
puppyImage = PhotoImage(file=galery[alpha])
puppyImage = resizeImage(puppyImage, 555, 550)
myCanvas.create_image(50, 50, anchor=NW, image=puppyImage)
start_btn = Button(text="Закончить просмотр",bg='black', fg='pink', font='calibri 30', command=end_see)
start_btn.place(x=190, y=0, height=100, width=515)
start_left = Button(text="НАЗАД", bg='black', fg='yellow', height=30,width=23,command=prev_rave)
start_left.pack(side=LEFT)
start_right = Button(text="ВПЕРЕД", bg='black', fg='yellow', height=30,width=24, command=next_rave)
start_right.pack(side=RIGHT)
root.mainloop()

