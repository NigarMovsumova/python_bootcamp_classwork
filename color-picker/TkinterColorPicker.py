from tkinter import *


def red():
    label.config(text='Red')
    entry.delete(0, END)
    entry.insert(0, '#ff0000')


def orange():
    label.config(text='Orange')
    entry.delete(0, END)
    entry.insert(0, '#ff7d00')


def yellow():
    label.config(text='Yellow')
    entry.delete(0, END)
    entry.insert(0, '#ffff00')


def green():
    label.config(text='Green')
    entry.delete(0, END)
    entry.insert(0, '#00ff00')


def cyan():
    label.config(text='Cyan')
    entry.delete(0, END)
    entry.insert(0, '#007dff')


def blue():
    label.config(text='Blue')
    entry.delete(0, END)
    entry.insert(0, '#0000ff')


def purple():
    label.config(text='Purple')
    entry.delete(0, END)
    entry.insert(0, '#7d00ff')


root = Tk()
root.title('Colors')
root.geometry('180x240')

label = Label(root, anchor='c')
label.pack()

entry = Entry(root, justify='center', bd=5)
entry.pack()

button1 = Button(width=16, bg='red', command=red)
button1.pack()

button2 = Button(width=16, bg='orange', command=orange)
button2.pack()
button3 = Button(width=16, bg='yellow', command=yellow)
button3.pack()
button4 = Button(width=16, bg='green', command=green)
button4.pack()
button5 = Button(width=16, bg='cyan', command=cyan)
button5.pack()
button6 = Button(width=16, bg='blue', command=blue)
button6.pack()
button7 = Button(width=16, bg='purple', command=purple)
button7.pack()

root.mainloop()
