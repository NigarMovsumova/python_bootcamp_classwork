from tkinter import *

# 1. contactlar filedan gelmelidir
# 2. her contact ya class obyekti, yada dict olmalidir.

root = Tk()
root.resizable(0, 0)
root.geometry('500x500')
root.config(bg='Blue')
root.title('List of People')

contactlist = [
    ['Elsad adaftir 28', '0702159014'],
    ['Talib Sederek Nar', '0702449574'],
    ['Muxtar Azer su azercell', '0512548778'],
    ['Qutab Tendir Satan Elmler', '0553215858'],
    ['Aga Selim usda ', '07021336555'],
    ['Elsen Moyka', '0702120505'],
]

name = StringVar()
number = StringVar()

frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=12)
select.pack(side=LEFT, fill=BOTH, expand=1)
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=select.yview)


def delete():
    del contactlist[selected()]
    person_info()


def addcontact():
    contactlist.append([name.get(), number.get()])
    person_info()


def selected():
    return int(select.curselection()[0])


def edit():
    contactlist[selected()] = [name.get(), number.get()]
    person_info()


def reset():
    name.set('')
    number.set('')


def view():
    name, phone = contactlist[selected()]
    name.set(name)
    number.set(phone)


def exit():
    root.destroy()


def person_info():
    contactlist.sort()
    select.delete(0, END)
    for name, phone in contactlist:
        select.insert(END, name)


person_info()
Label(root, text='Number of Person', font='arial 12 bold', bg='gold').place(x=30, y=70)
Entry(root, textvariable=number).place(x=180, y=70)

Label(root, text='Name of the Contact', font='arial 12 bold', bg='Pink').place(x=30, y=20)
Entry(root, textvariable=name).place(x=100, y=40)

Button(root, text=" Add the Person", font='arial 12 bold', bg='Green', command=addcontact).place(x=50, y=110)
Button(root, text="Edit Person Info", font='arial 12 bold', bg='Yellow', command=edit).place(x=50, y=260)

Button(root, text="Close the Window", font='arial 12 bold', bg='Grey', command=exit).place(x=200, y=320)
Button(root, text="Reset", font='arial 12 bold', bg='White', command=reset).place(x=50, y=310)

Button(root, text="Delete", font='arial 12 bold', bg='Red', command=delete).place(x=50, y=210)
Button(root, text="View", font='arial 12 bold', bg='Orange', command=view).place(x=50, y=160)

root.mainloop()
