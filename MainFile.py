from tkinter import *


def create_new_window():
    new_root_window = Tk()
    new_root_window.title('Main File')
    new_root_window.geometry('500x500')
    new_button = Button(new_root_window, text='test')
    new_button.pack()
    new_root_window.mainloop()
