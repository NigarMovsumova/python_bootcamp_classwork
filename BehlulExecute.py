from functools import partial
from tkinter import *

def dye_bg_red():
    file.configure(bg='red')


def dye_bg_yellow():
    file.configure(bg='yellow')


def hello_counter():
    return count


def dye_bg_green():
    file.configure(bg='green')


def write_hello():
    global count
    if len(hello_list) <= 9:
        count = count + 1
        label = Label(file, text=f'Hello {len(hello_list)},', font=('Arial', 10, 'bold'))
        label.config(bd=10)
        label.pack(anchor='nw')
        hello_list.append(label)
    return hello_list


def delete_hello():
    hello_list[-1].destroy()
    hello_list.pop()


file = Tk()
file.title('Write Hello')
file.geometry('500x550')


hello_list = []
count = 0

label = Label(file, width=4, height=1)
label.place(x=427, y=0)

plus_button = Button(text='+', width=5, command=write_hello)
plus_button.pack(anchor='ne')

minus_button = Button(text='-', width=5, command=partial(delete_hello))
minus_button.place(x=386, y=0)

execute_button = Button(text='Execute', width=15, command=write_hello)
execute_button.pack(anchor='ne')

red_button = Button(text='Red', bg='red', width=15, command=dye_bg_red)
red_button.pack(anchor='ne')

yellow_button = Button(text='Yellow', bg='yellow', width=15, command=dye_bg_yellow)
yellow_button.pack(anchor='ne')

green_button = Button(text='Green', bg='green', width=15, command=dye_bg_green)
green_button.pack(anchor='ne')

file.mainloop()
