from tkinter import *
# https://data-flair.training/blogs/address-book-in-python/
root = Tk()
root.geometry('400x400')
root.config(bg='light blue')
root.resizable(0, 0)
root.title('My Contact')

# 1. Contactlar file-da yazilmalidir
# 2. contact ya object olmalidir, ve ya dictionary olmalidir.
my_contact = [
    ['Vidadi Rzayev', '055550302'],
    ['Sahib Cabbarov', '0708586523'],
    ['Ismayil Raperican ', '0775609393'],
    ['Yusif Cabbarzade(me)', '0708811010'],
    ['Mama', '0704466247'],
    ['Ata', '0705522012'],
]

Name = StringVar()
Number = StringVar()

frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=15)
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=BOTH, expand=1)
# select.pack(side=RIGHT, fill=BOTH, expand=1)


def Selected():
    return int(select.curselection()[0])


def AddContact():
    my_contact.append([Name.get(), Number.get()])
    Select_set()
    pass


def EDIT():
    my_contact[Selected()] = [Name.get(), Number.get()]
    Select_set()
    pass


def DELETE():
    del my_contact[Selected()]
    Select_set()
    pass


def VIEW():
    NAME, PHONE = my_contact[Selected()]
    Name.set(NAME)
    Number.set(PHONE)
    pass


def EXIT():
    root.destroy()
    pass


def RESET():
    Name.set('')
    Number.set('')
    pass


def Select_set():
    my_contact.sort()
    select.delete(0, END)
    for name, phone in my_contact:
        select.insert(END, name)


Select_set()

Label(root, text='NAME', font=' Lao 12  ', bg='azure', fg='dodgerblue').place(x=1, y=80)
Entry(root, textvariable=Name).place(x=54, y=80)

Label(root, text='PHONE NO.', font='Lao 12  ', bg='azure', fg='dodgerblue').place(x=1, y=105)
Entry(root, textvariable=Number).place(x=96, y=105)

Button(root, text="ADD", font='arial 12 ', bg='azure', fg='dodgerblue', command=AddContact).place(x=66, y=0)
Button(root, text="EDIT", font='arial 12 ', bg='azure', fg='dodgerblue', command=EDIT).place(x=113, y=0)

Button(root, text="DELETE", font='arial 12 ', bg='azure', fg='dodgerblue', command=DELETE).place(x=210, y=0)
Button(root, text="VIEW", font='arial 12 ', bg='azure', fg='dodgerblue', command=VIEW).place(x=160, y=0)

Button(root, text="EXIT", font='arial 12 ', bg='brown', fg='dodgerblue', command=EXIT).place(x=350, y=0)
Button(root, text="RESET", font='arial 12  ', bg='azure', fg='dodgerblue', command=RESET).place(x=285, y=0)

root.mainloop()

