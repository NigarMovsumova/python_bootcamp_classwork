from functools import partial
from tkinter import *
from tkinter import Entry

list = []


def multiply():
    list.append(entry.get())
    list.append("*")
    entry.delete(0, END)


def create_operation_buttons():
    multiplication = Button(root, text='*', fg='black', bg='WHITE', height=1, width=7, command=multiply)
    multiplication.pack()

    equals_button = Button(root, text='=', fg='black', bg='WHITE', height=1, width=7, command=equals)
    equals_button.pack()


def equals():
    list.append(entry.get())
    entry.delete(0, END)
    entry.insert(0, list)


def create_digit_buttons():
    buttons_list = []
    for i in range(0, 10):
        button = Button(root, text=i, fg='black', bg='WHITE', height=1, width=7,
                        command=partial(insert_number, i))
        button.pack()
        buttons_list.append(button)


def insert_number(number):
    user_input = entry.get() + str(number)

    entry.delete(0, END)
    entry.insert(0, user_input)


root = Tk()
root.title('Calculator')
root.geometry('400x500')
root.configure()
user_input = ""

expression = ""
entry = Entry(width=30)
entry.insert(0, '')
entry.pack()

create_digit_buttons()
create_operation_buttons()

root.mainloop()
