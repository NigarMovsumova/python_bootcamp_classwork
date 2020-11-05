from functools import partial
from tkinter import *


def show_color(color_name):
    entry.delete(0, END)
    entry.insert(0, color_name)


def create_buttons():
    colors_list = ['red', 'green', 'blue', 'black', 'orange', 'violet', 'cyan']
    buttons_list = []
    for i in range(0, 7):
        button = Button(width=16, bg=colors_list[i], command=partial(show_color, colors_list[i]))
        buttons_list.append(button)
        button.pack()


root = Tk()
root.title('Colors')
root.geometry('180x240')

label = Label(root, anchor='c')
label.pack()

entry = Entry(root, justify='center', bd=5)
entry.pack()

create_buttons()

root.mainloop()
