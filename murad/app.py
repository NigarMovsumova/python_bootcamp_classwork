from tkinter import *
from tkinter import messagebox
import json


root_window = Tk()

root_window.title("Contact")
root_window.config(bg="SlateGray3")
root_window.resizable(0, 0)

window_width = 900
window_height = 600

screen_width = root_window.winfo_screenwidth()
screen_height = root_window.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

phone_number = [
    # {"name": "Murad", "surname": "Suleymanov", "phone number №1": "0503737496", "phone number №2": "0554284475",
    #  "email": "suleymanovmurad@gmail.com", "address": "Emin Sabitoglu kuchesi"},
    # {"name": "Huseyn", "surname": "Memmedov", "phone number №1": "0708883457", "phone number №2": "",
    #  "email": "suleymanovmurad@gmail.com", "address": "Emin Sabitoglu kuchesi"},
    # {"name": "Ruslan", "surname": "Mustafayev", "phone number №1": "0774326574", "phone number №2": "",
    #  "email": "mustafayevruslan@gmail.com", "address": "Bakixanov kuchesi"},
    # {"name": "Intiqam", "surname": "Pashayev", "phone number №1": "0554573275", "phone number №2": "0772425462",
    #  "email": "pashayevintiqam@gmail.com", "address": "Xan Shushuniski kuchesi"},
    # {"name": "Behruz", "surname": "Huseynov", "phone number №1": "0702148593", "phone number №2": "",
    #  "email": "huseynovbehruz@gmail.com", "address": "Dilare Eliyeva kuchesi"},
    # {"name": "Yusif", "surname": "Atakishiyev", "phone number №1": "0553258784", "phone number №2": "0504311122",
    #  "email": "atakishiyevyusif@gmail.com", "address": "Seyidov kuchesi"},
    # {"name": "Pervin", "surname": "Aliyev", "phone number №1": "0554235434", "phone number №2": "",
    #  "email": "aliyevpervin@gmail.com", "address": "Cavadxan kuchesi"},
    # {"name": "Anar", "surname": "Mirzeyev", "phone number №1": "0504344385", "phone number №2": "",
    #  "email": "mirzeyevanar@gmail.com", "address": "Feteli Khan Khoyiski kuchesi"},
    # {"name": "Mehemmed", "surname": "Salehov", "phone number №1": "0556899832", "phone number №2": "",
    #  "email": "salehovmehemmed@gmail.com", "address": "Genclik kuchesi"},
    # {"name": "Murad", "surname": "Abdullayev", "phone number №1": "0994336573", "phone number №2": "0509943365",
    #  "email": "abdullayevmurad189@gmail.com", "address": "Beshir Seferoglu kuchesi"},
    # {"name": "Samir", "surname": "Mahirov", "phone number №1": "0504658665", "phone number №2": "",
    #  "email": "mahirovsamir189@gmail.com", "address": "Nizami kuchesi"}
]

name = StringVar()
surname = StringVar()
first_number = StringVar()
second_number = StringVar()
email = StringVar()
address = StringVar()

frame = Frame(root_window)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
listbox = Listbox(frame, yscrollcommand=scroll.set, height=17, width=27)
scroll.config(command=listbox.yview)
scroll.pack(side=RIGHT, fill=Y)
listbox.pack(side=LEFT, fill=BOTH, expand=1)


def selected():
    return int(listbox.curselection()[0])


def add_contact():
    contact = {"name": name.get(), "surname": surname.get(), "phone number №1": first_number.get(),
               "phone number №2": second_number.get(), "email": email.get(), "address": address.get()}
    phone_number.append(contact)
    with open('contact', 'a+') as f:
        f.write(json.dumps(contact) + '\n')
    select_set()


def edit():
    phone_number[selected()] = contact = {"name": name.get(), "surname": surname.get(),
                                          "phone number №1": first_number.get(),
                                          "phone number №2": second_number.get(), "email": email.get(),
                                          "address": address.get()}
    select_set()


def delete():
    del phone_number[selected()]
    select_set()


def view():
    contact_name = phone_number[selected()]['name']
    contact_surname = phone_number[selected()]['surname']
    # NAME, SURNAME, FIRST_NUMBER, SECOND_NUMBER, EMAIL, ADDRESS = phone_number[selected()]
    name.set(contact_name)
    surname.set(contact_surname)
    # first_number.set(FIRST_NUMBER)
    # second_number.set(SECOND_NUMBER)
    # email.set(EMAIL)
    # address.set(ADDRESS)


def exit():
    messagebox.askyesno(title="Informed", message="Are you sure you want to go out?")
    root_window.destroy()


def reset():
    name.set(" ")
    surname.set(" ")
    first_number.set(" ")
    second_number.set(" ")
    email.set(" ")
    address.set(" ")


def read_contact():
    with open("contact", "r") as content:
        lines = content.readlines()
        for line in lines:
            contact = json.loads(line)
            phone_number.append(contact)


def select_set():
    read_contact()
    listbox.delete(0, END)
    for contact in phone_number:
        listbox.insert(END, contact["name"])


select_set()

Label(text="Name", font="Calibri 18 bold", bg="SlateGray3").place(x=30, y=20)
Entry(textvariable=name).place(x=160, y=30)

Label(text="Surname", font="Calibri 18 bold", bg="SlateGray3").place(x=30, y=70)
Entry(textvariable=surname).place(x=160, y=80)

Label(text="Number №1", font="Calibri 18 bold", bg="SlateGray3").place(x=30, y=120)
Entry(textvariable=first_number).place(x=160, y=130)

Label(text="Number №2", font="Calibri 18 bold", bg="SlateGray3").place(x=30, y=170)
Entry(textvariable=second_number).place(x=160, y=180)

Label(text="Email", font="Calibri 18 bold", bg="SlateGray3").place(x=30, y=220)
Entry(textvariable=email).place(x=160, y=230)

Label(text="Address", font="Calibri 18 bold", bg="SlateGray3").place(x=30, y=270)
Entry(textvariable=address).place(x=160, y=280)

Button(text="ADD", font="Calibri 18 bold", bg="SlateGray4", width=7, height=1, command=add_contact).place(x=50, y=330)
Button(text="VIEW", font="Calibri 18 bold", bg="SlateGray4", width=7, height=1, command=view).place(x=50, y=390)
Button(text="DELETE", font="Calibri 18 bold", bg="SlateGray4", width=7, height=1, command=delete).place(x=50, y=450)
Button(text="EDIT", font="Calibri 18 bold", bg="SlateGray4", width=7, height=1, command=edit).place(x=160, y=330)
Button(text="RESET", font="Calibri 18 bold", bg="SlateGray4", width=7, height=1, command=reset).place(x=160, y=390)
Button(text="EXIT", font="Calibri 18 bold", bg="Tomato", width=7, height=1, command=exit).place(x=790, y=460)

root_window.mainloop()
