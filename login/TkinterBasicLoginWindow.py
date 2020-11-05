from tkinter import *


def insert():
    username_label.insert(0, 'Hello ')
    password_label.delete(0, END)


def delete():
    username_label.delete(0, END)
    password_label.delete(0, END)


root_window = Tk()

root_window.title('Login')

root_window.geometry('300x200')

label = Label(text='Welcome to Facebook:', font=('Arial', 16, 'bold'))
label.config(bd=10)
label.pack()

username_label = Entry(width=30)
username_label.insert(0, 'Your username')
username_label.pack()

password_label = Entry(width=30)
password_label.insert(0, 'Your password')
password_label.pack()

login_button = Button(text='Login', bg='#ffffff', fg='#000000', width=10, height=1)
login_button.config(command=insert)
login_button.pack(side=LEFT, padx=30, pady=15)

delete_button = Button(text='Delete', bg='#ffffff', fg='#000000', width=10, height=1)
delete_button.config(command=delete)
delete_button.pack(side=RIGHT, padx=30, pady=15)

root_window.mainloop()
