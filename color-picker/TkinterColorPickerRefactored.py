from tkinter import *

def red():
    label.config(text='red')
    color_code.delete(0, END)
    color_code.insert(0, '#ff0000')


def black():
    label.config(text='black')
    color_code.delete(0, END)
    color_code.insert(0, '#ff7d00')


def green():
    label.config(text='green')
    color_code.delete(0, END)
    color_code.insert(0, '#00ff00')


def orange():
    label.config(text='orange')
    color_code.delete(0, END)
    color_code.insert(0, '#ff7d00')


def yellow():
    label.config(text='yellow')
    color_code.delete(0, END)
    color_code.insert(0, '#ffff00')


def cyan():
    label.config(text='cyan')
    color_code.delete(0, END)
    color_code.insert(0, '#007dff')


def violet():
    label.config(text='violet')
    color_code.delete(0, END)
    color_code.insert(0, '#007dff')


root = Tk()
root.title('Color Picker Game')
root.geometry('250x300')

label = Label(root)
label.pack()

color_code = Entry(root, justify='center', bd=5)
color_code.pack()

button1 = Button(width=16, bg='red', command=red)
button1.pack()

button1 = Button(width=16, bg='black', command=black)
button1.pack()

button1 = Button(width=16, bg='green', command=green)
button1.pack()

button1 = Button(width=16, bg='orange', command=orange)
button1.pack()

button1 = Button(width=16, bg='yellow', command=yellow)
button1.pack()

button1 = Button(width=16, bg='cyan', command=cyan)
button1.pack()

button1 = Button(width=16, bg='violet', command=violet)
button1.pack()

root.mainloop()
