from tkinter import *
import json

root = Tk()
root.geometry('400x400')
root.config(bg='darkseagreen')
root.resizable(0, 0)
root.title('AddressBook')

contact_list = [
    # ['Fidan', 'Memmedova', '0176738493', 'Baku', 'fidanm@gmail.com'],
    # ['David', 'Babayev', '2684430000', 'Baku', 'daviddba@gmail.com'],
    # ['Medina', 'Bayramli', '4338354432', 'Quba', 'bayramlie@gmail.com'],
    # ['Nuray', 'Adisirinli', '6834552341', 'Baku', 'nuraayya@gmail.com'],
    # ['Raul', 'Abbasov', '1234852689', 'Sumqayit', 'vraul@gmail.com'],
    # ['Sema', 'Memmedli', '2119876543', 'Quba', 'semaam@gmail.com'],
    # ['Murad', 'Babayev', '2273846729', 'Baku', 'babayevv@gmail.com'],
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
    contact_list.append([Name.get(), Phone.get()])
    select_set()


def edit():
    contact_list[selected()] = [Name.get(), Surname.get(), Phone.get(),
                                Address.get(), Email.get()]
    select_set()


def delete():
    del contact_list[selected()]
    select_set()


def view():
    name, surname, phone, address, email = contact_list[selected()]
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

# import json
#
# sample_dict = {"name": "Nigar", "surname": "Movsumova"}
# with open('users', 'a+') as f:
#     f.write(json.dumps(sample_dict) + '\n')
#
# with open('users', 'r') as f:
#     sample_dict_str = f.readline()
#     print(type(sample_dict_str))
#     print(sample_dict_str)
#     converted_dict = json.loads(sample_dict_str)
#     print(converted_dict)
#     print(type(converted_dict))
#     print(converted_dict['name'])
#     print(converted_dict['surname'])
#     # print(f.readline())

def read_contacts():
    with open('contacts/contact_book', 'r') as content:
        lines = content.read().splitlines()
        for line in lines:
            contact = json.loads(line)
            contact_list.append(contact)
    print(contact_list)


def select_set():
    read_contacts()
    contact_list.sort()
    select.delete(0, END)
    for name, surname, phone, address, email in contact_list:
        select.insert(END, name)


select_set()

Label(root, text='NAME', font='arial 13 bold', bg='Slategray3').place(x=10, y=20)
Entry(root, textvariable=Name).place(x=130, y=20)

Label(root, text='SURNAME', font='arial 13 bold', bg='Slategray3').place(x=10, y=40)
Entry(root, textvariable=Surname).place(x=130, y=40)

Label(root, text='ADDRESS', font='arial 13 bold', bg='Slategray3').place(x=10, y=60)
Entry(root, textvariable=Address).place(x=130, y=60)

Label(root, text='PHONE NO', font='arial 13 bold', bg='Slategray3').place(x=10, y=80)
Entry(root, textvariable=Phone).place(x=130, y=80)

Label(root, text='EMAIL', font='arial 13 bold', bg='Slategray3').place(x=10, y=100)
Entry(root, textvariable=Email).place(x=130, y=100)

Button(root, text=" ADD", font='arial 12 bold', bg='Slategray3', command=add_contact).place(x=20, y=200)
Button(root, text="EDIT", font='arial 12 bold', bg='Slategray3', command=edit).place(x=74, y=200)
Button(root, text="DELETE", font='arial 12 bold', bg='Slategray3', command=delete).place(x=126, y=200)

Button(root, text="VIEW", font='arial 12 bold', bg='Slategray3', command=view).place(x=20, y=240)
Button(root, text="RESET", font='arial 12 bold', bg='Slategray3', command=reset).place(x=77, y=240)
Button(root, text="EXIT", font='arial 12 bold', bg='red', command=exit).place(x=302, y=320)

root.mainloop()
