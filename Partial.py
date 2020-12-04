from tkinter import *
from functools import partial


def on_click(button_to_forget):
    button_to_forget.pack_forget()


root_window = Tk()

root_window.title('Partial')
root_window.geometry('250x250')

button = Button(text='Hello')
button.pack()
button.configure(command=partial(on_click, button))
root_window.mainloop()
