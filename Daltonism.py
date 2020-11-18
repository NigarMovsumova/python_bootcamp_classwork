from random import randint
from tkinter import *

'''
1. İstifadəçinin daltonik olub olmadığını yoxlamaq üçün nəzərdə tutulmuş proqram yazmaq gərəkir.
10 seçim verilir istifadəçi seçim etdikcə və istifadəçi gördüyü rəngin nə rəng olduğunu seçir 4 variantdan
(1 düz, digərləri random).
'''


def create_buttons():
    buttons = []
    for i in range(0, 4):
        button = Button(text= '', width=12, font='verdana 8 bold', bd=2)
        button.place(x=124, y=110)
        button.pack()
        buttons.append(button)
    return buttons


def next_color():
    correct_color = color_list[randint(0, len(color_list) - 1)]
    square.config(bg=correct_color)
    correct_color_index = randint(0, 3)
    buttons_list[correct_color_index].config(text=correct_color)
    for i in range(len(buttons_list)):
        if i != correct_color_index:
            buttons_list[i].config(text = 'blue')

window = Tk()
window.title('Daltonism Test')
window.geometry('350x350')

color_list = ['black', 'yellow', 'blue', 'green', 'grey', 'orange', 'red', 'brown']
correct_color = 'white'

square = Canvas(height=100, width=100, bg='black')
square.pack()

buttons_list = create_buttons()

next = Button(text='NEXT', width=12, bg='white', font='verdana 8 bold', command=next_color)
next.place(x=124, y=230)

window.mainloop()
