from tkinter import *


def login():
    username.insert(0, 'Hello ')


def delete():
    username.delete(0, END)
    password.delete(0, END)


root_window = Tk()
root_window.title('Login')
root_window.geometry('350x600')

label = Label(text='Welcome to PointBlank', font=('Arial', 15, 'bold'))
label.pack()

username = Entry(width=30)
username.pack()

password = Entry(width=30)
password.pack()

login_button = Button(text='Login')
login_button.config(command=login)
login_button.pack()

delete_button = Button(text='Delete')
delete_button.config(command=delete)
delete_button.pack()

root_window.mainloop()
