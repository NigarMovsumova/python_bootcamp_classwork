import pickle
from tkinter import *
from tkinter import messagebox

HEIGHT = 550
WIDTH = 550


def login_form():
    frame = Frame(root, bd=10)
    frame.place(relx=0.5, rely=0.2, relwidth=0.7, relheight=0.6, anchor='n')
    # Sign in text label
    label = Label(frame, text='Sign In', font='16')
    label.place(relwidth=1, relheight=0.1)
    # Login
    label_login = Label(frame, text='Login: ')
    label_login.place(rely=0.2, relwidth=0.35, relheight=0.1)
    enter_login = Entry(frame)
    enter_login.place(relx=0.4, rely=0.2, relheight=0.1, relwidth=0.55)
    # Password
    label_password = Label(frame, text='Password: ')
    label_password.place(rely=0.4, relwidth=0.35, relheight=0.1)
    enter_password = Entry(frame, show='*')
    enter_password.place(relx=0.4, rely=0.4, relheight=0.1, relwidth=0.55)

    button = Button(frame, text='Sign in', command=lambda: login_pass())
    button.place(relx=0.3, rely=0.8, relheight=0.15, relwidth=0.5)

    def login_pass():
        f = open('login.txt', 'rb')
        a = pickle.load(f)
        f.close()
        if enter_login.get() in a and enter_password.get() == a[enter_login.get()]:
            messagebox.showinfo('Welcome', 'Welcome to the Game.')
        else:
            messagebox.showerror('Error!', 'Invalid login or password')


def registration():
    label_error = None
    frame = Frame(root, bd=10)
    frame.place(relx=0.5, rely=0.2, relwidth=0.7,
                relheight=0.6, anchor='n')
    # Sign in text label
    label = Label(frame, text='Sign Up', font='16')
    label.place(relwidth=1, relheight=0.1)
    # Login
    label_login = Label(frame, text='Login: ')
    label_login.place(rely=0.2, relwidth=0.35, relheight=0.1)
    login_register = Entry(frame)
    login_register.place(relx=0.4, rely=0.2, relheight=0.1, relwidth=0.55)
    label_password1 = Label(frame, text='Password: ')
    label_password1.place(rely=0.4, relwidth=0.35, relheight=0.1)
    password1 = Entry(frame, show='*')
    password1.place(relx=0.4, rely=0.4, relheight=0.1, relwidth=0.55)
    label_password2 = Label(frame, text='Confirm password: ')
    label_password2.place(rely=0.6, relwidth=0.35, relheight=0.1)
    password2 = Entry(frame, show='*')
    password2.place(relx=0.4, rely=0.6, relheight=0.1, relwidth=0.55)
    button = Button(frame, text='Sign up', command=lambda: signup())
    button.place(relx=0.3, rely=0.8, relheight=0.15, relwidth=0.5)

    def signup():
        nonlocal label_error
        error = ''
        if label_error:
            label_error.destroy()
        # Error label
        if len(login_register.get()) == 0:
            error = '*login error'
        elif len(password1.get()) < 6:
            error = '*your password needs to be at least 6 character'
        elif not password1.get() == password2.get():
            error = '*password error'
        else:
            save()
        label_error = Label(frame, text=error, fg='red')
        label_error.place(rely=0.7)

    def save():
        data = dict()
        data[login_register.get()] = password1.get()
        f = open('login.txt', 'wb')
        pickle.dump(data, f)
        f.close()
        login_form()


root = Tk()
root.title('Login Form')
root.geometry("%dx%d" % (WIDTH, HEIGHT))
root.resizable(False, False)
root.option_add('*Font', 'Calibri')
root.option_add('*Background', 'white')

img = PhotoImage(file='img/black-background.gif')
background_label = Label(root, image=img)
background_label.place(relwidth=1, relheight=1)

button_signup = Button(root, text='SIGN UP', bg='gold', command=registration)
button_signup.place(relx=0.2, rely=0.1, relwidth=0.3)
button_signin = Button(root, text='SIGN IN', bg='gold', command=login_form)
button_signin.place(relx=0.5, rely=0.1, relwidth=0.3)

root.mainloop()
