from tkinter import *
from tkinter.ttk import *

import MainFile

root_window = Tk()

root_window.title('Main menu')
root_window.geometry('500x500')

button = Button(text='test', command=MainFile.create_new_window)
button.pack()

root_window.mainloop()
