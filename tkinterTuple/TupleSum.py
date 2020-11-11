from tkinter import *

root_window = Tk()
root_window.title('Tuple Sum')
root_window.geometry('100x100')

tuple_entry = Entry(root_window, justify='center', bd=5)
tuple_entry.pack()

ok_button = Button(width=16, bg='blue')
ok_button.pack()

label = Label(root_window, anchor='c')
label.pack()

numbers = []
numbers = tuple_entry.get().split()

root_window.mainloop()
