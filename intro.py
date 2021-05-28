from tkinter import *


def enter_password(event):
    password.delete(0, len(password.get()))
    password.config(show='*')


def login():
    admin_username = 'NigarMovsum'
    admin_password = 'Step2020!'
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
username = Entry(width=50)
# username.insert(0, 'trololo')
username.insert(0, 'Enter the username')
username.pack()

password = Entry(width=50)
password.insert(0, 'Enter the password')
password.bind('<FocusIn>', enter_password)

password.pack()

button = Button(text='Press Me!', command=login, width=50, height=1)
button.pack()

root_window.mainloop()

# 1. Tkinterde password-u baglamaq
# 2. Entrynin ve Buttonun olchulerini deyishmek
# 3. Usernamedede ele etmek lazimdir, men uzerine basan kimi
# username fieldin yazilar pozulsun.
# 4. Her defe yeni label yaradilmasin, eyni label-in
# yazisi deyishsin.

