from tkinter import *
from tkinter import messagebox

root_window = Tk()
root_window.title('Charlie has something to tell you')
root_window.geometry('500x500')

img = PhotoImage(file='img/charlie.gif')
background_label = Label(root_window, image=img)
background_label.place(relwidth=1, relheight=1)

messagebox.showinfo('Welcome', 'Welcome to the Game.')
messagebox.showerror('Error', 'You made an error')
messagebox.showwarning('Warning', 'Warning sample message')

root_window.mainloop()
