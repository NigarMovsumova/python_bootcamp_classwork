from tkinter import *

root = Tk()
root.geometry('400x400')
root.config(bg='darkseagreen')
root.resizable(0, 0)
root.title('ContactBook')

my_dict = [
    {"name": "Fidan", "surname": "Memmedova", "phone": "48395749573",
"address": "Baku", "email": "fidanm@gmail.com"},
    {"name": "David", "surname": "Babayev", "phone": "23878233",
"address": "Quba", "email": "davidb@gmail.com"},
    {"name": "Medina", "surname": "Bayramli", "phone": "749474934",
"address": "Baku", "email": "medinab@gmail.com"},
    {"name": "Nuray", "surname": "Adisirinli", "phone": "89392382",
"address": "Baku", "email": "nurayaa@gmail.com"},
    {"name": "Raul", "surname": "Abbasov", "phone": "02372947294",
"address": "Quba", "email": "raula@gmail.com"},
    {"name": "Sema", "surname": "Memmedli", "phone": "8394639472",
"address": "Baku", "email": "msema@gmail.com"}
]

Name = StringVar()
Surname = StringVar()
Phone = StringVar()
Address = StringVar()
Email = StringVar()

frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=14)
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)


def selected():
    return int(select.curselection()[0])


def add_contact():
    contact = {'name': Name.get(), 'surname':Surname.get(),
               'phone': Phone.get(), 'address':Address.get(),
               'email': Email.get()}
    my_dict.append(contact)
#     my_dict.append([Name.get(), Surname.get(), Phone.get(), Address.get(),
# Email.get()])
    select_set()


def edit():
    my_dict[selected()] = [Name.get(), Surname.get(), Phone.get(),
Address.get(), Email.get()]
    select_set()


# def delete():
#     del my_dict.append()[selected()]
#     select_set()


def view():
    name, surname, phone, address, email = my_dict.append()[selected()]

    Name.set(name)
    Surname.set(surname)
    Phone.set(phone)
    Address.set(address)
    Email.set(email)


def exit_app():
    root.destroy()


def reset():
    Name.set('')
    Surname.set('')
    Phone.set('')
    Address.set('')
    Email.set('')


def select_set():
    # my_dict.sort()
    select.delete(0, END)
    # for name, surname, phone, address, email in my_dict:
    #     select.insert(END, name)
    for contact in my_dict:
        select.insert(END, contact['name'])


select_set()

Label(root, text='NAME', font='arial 13 bold',
bg='Slategray3').place(x=10, y=20)
Entry(root, textvariable=Name).place(x=130, y=20)

Label(root, text='SURNAME', font='arial 13 bold',
bg='Slategray3').place(x=10, y=40)
Entry(root, textvariable=Surname).place(x=130, y=40)

Label(root, text='PHONE NO', font='arial 13 bold',
bg='Slategray3').place(x=10, y=80)
Entry(root, textvariable=Phone).place(x=130, y=80)

Label(root, text='ADDRESS', font='arial 13 bold',
bg='Slategray3').place(x=10, y=60)
Entry(root, textvariable=Address).place(x=130, y=60)

Label(root, text='EMAIL', font='arial 13 bold',
bg='Slategray3').place(x=10, y=100)
Entry(root, textvariable=Email).place(x=130, y=100)

Button(root, text=" ADD", font='arial 12 bold', bg='Slategray3',
command=add_contact).place(x=20, y=200)
Button(root, text="EDIT", font='arial 12 bold', bg='Slategray3',
command=edit).place(x=74, y=200)
# Button(root, text="DELETE", font='arial 12 bold', bg='Slategray3',
# command=delete).place(x=126, y=200)

Button(root, text="VIEW", font='arial 12 bold', bg='Slategray3',
command=view).place(x=20, y=240)
Button(root, text="RESET", font='arial 12 bold', bg='Slategray3',
command=reset).place(x=77, y=240)
Button(root, text="EXIT", font='arial 12 bold', bg='red',
command=exit).place(x=302, y=320)

root.mainloop()
