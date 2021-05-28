from tkinter import *


def print_to_terminal():
    admin_username = 'NigarMovsum'
    admin_password = 'Step2020!'
    # print('Username =', username.get())
    # print('Password =', password.get())
    if username.get() == admin_username and admin_password == password.get():
        successful_login_label = Label(text='You are successfully logged in')
        successful_login_label.pack()
    else:
        unsuccessful_login_label = Label(text='Username or Password is wrong')
        unsuccessful_login_label.pack()


root_window = Tk()
root_window.title('Game App')
root_window.geometry('500x500')
# fg = foreground color
# bg = background color
label = Label(text='Welcome to the Game App:', font=('Arial', 25),
              fg='red', bg='black')
label.pack()
username = Entry()
username.insert(0, 'Enter the username')
username.pack()

password = Entry()
password.insert(0, 'Enter the password')
password.pack()

button = Button(text='Press Me!', command=print_to_terminal)
button.pack()


root_window.mainloop()

# 1. Tkinterde password-u baglamaq
# 2. Entrynin ve Buttonun olchulerini deyishmek
