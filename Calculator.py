# 1. kalkulyator
# 2. 2 eded daxil etmeye imkan var.
# 3. vurma duymesi
# 4. netice chap olunur

from tkinter import *


def multiply():
    try:
        label.config(text=int(first_entry.get()) * int(second_entry.get()))
    except ValueError:
        label.config(text='Enter valid numbers', font='Arial 8 bold')


root_window = Tk()
root_window.title('Calculator')
root_window.geometry('300x200')
root_window.configure(background='beige')

label = Label(text='Calculator', font=('Arial', 16, 'bold'))
label.config(bd=10)
label.pack()

first_entry = Entry(width=30)
first_entry.insert(0, 'Enter first number:')
first_entry.pack()

second_entry = Entry(width=30)
second_entry.insert(0, 'Enter second number:')
second_entry.pack()

multiplication_button = Button(text=' * ', bg='#F2D9F3', fg='#000000', width=10, height=1, command=multiply)
multiplication_button.pack(side=LEFT, padx=58, pady=20)

label = Label(text='', font=('Arial', 16, 'bold'))
label.config(bd=10)
label.pack(side=RIGHT, padx=10, pady=20)

root_window.mainloop()
