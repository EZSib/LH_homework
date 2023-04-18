from turtle import *

'''1. Используя модуль turtle, придумай логотип своей IT-компании, который должен содержать
в себе геометрические фигуры и текст.
'''
pensize(5)
bgcolor("darkgrey")
color('red', 'black')
begin_fill()
circle(160)
end_fill()
penup()
goto(-128, 80)
pendown()
color('darkviolet', 'red')
begin_fill()
for _ in range(3):
    forward(260)
    left(120)
end_fill()
penup()
goto(-54, 90)
pendown()
pensize(1)
color('darkgreen', 'darkviolet')
begin_fill()
for _ in range(4):
    forward(110)
    left(90)
end_fill()
color('chartreuse1')
write("EZ", font=("italic", 65, "normal"))
exitonclick()
'''2. Используя модуль pillow, придумай логотип своей IT-компании, который должен содержать
в себе геометрические фигуры и текст. Сохрани логотип в формате .png.'''

from PIL import Image, ImageFont, ImageDraw

img = Image.new('RGB', (200, 200), (171, 176, 179))
idraw = ImageDraw.Draw(img)
idraw.ellipse((0, 0, 200, 200), outline=(201, 20, 20) , width=3, fill=(0, 0, 0))
idraw.polygon([(30,30), (170, 30), (100,200)],width=3, fill = (201, 20, 20), outline=(198, 20, 201))
idraw.rectangle(((60,35),(140,100)),width=1, fill = (177, 4, 212), outline=(12, 207, 194))
text = "EZ"
font = ImageFont.truetype('arial', 60)
idraw.text((60, 30), text, fill=(7, 235, 90), font=font )
img.save('learnup.png')



