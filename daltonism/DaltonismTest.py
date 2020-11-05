from tkinter import *
from functools import partial
import random


def create_buttons():
    buttons = []
    for i in range(0, 4):
        choice_button = Button(text='', bg='#ffffff', fg='#000000', width=10, height=1)
        choice_button.pack()
        buttons.append(choice_button)
    return buttons


def show_color(i):
    color = random.choices(random_colors)
    rectangle = canvas.create_rectangle(0, 0, 600, 600, fill=color)
    i += 1
    update_labels(color)
    return rectangle


def update_labels(color):
    given_choices = random.choices(random_colors + color)
    for i in range(0, len(buttons_list)):
        buttons_list[i].config(text=given_choices[i])
        buttons_list[i].pack()


root_window = Tk()
root_window.title('Daltonism Test')
root_window.geometry('700x700')

random_colors = ['white', 'red', 'blue', 'green', 'brown', 'black', 'yellow', 'violet']

canvas = Canvas(root_window, width=100, height=100)
canvas.pack()

buttons_list = create_buttons()

i = 0
next_button = Button(text='Next', bg='#ffffff', fg='#000000', width=10, height=1, command= partial(show_color, i))
next_button.pack()

root_window.mainloop()
