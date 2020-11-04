from tkinter import *
from functools import partial


def show_color(color_name):
    color_code.delete(0, END)
    color_code.insert(0, color_name)


def create_buttons():
    colors_list = ['red', 'green', 'black', 'yellow', 'blue', 'cyan', 'orange']
    buttons_list = []
    for i in range(0, 7):
        button1 = Button(width=16, bg=colors_list[i], command=partial(show_color, colors_list[i]))
        buttons_list.append(button1)
        button1.pack()
    return buttons_list


root = Tk()
root.title('Color Picker Game')
root.geometry('250x300')

label = Label(root)
label.pack()

color_code = Entry(root, justify='center', bd=5)
color_code.pack()

buttons = create_buttons()

root.mainloop()
