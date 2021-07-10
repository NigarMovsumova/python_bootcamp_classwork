import tkinter as tk

window = tk.Tk()
window.title('Phone book')
window.geometry('600x500')
window.configure(bg='PaleTurquoise2')
window.attributes('-alpha', 0.9)
dates = []
update_book = []

contacts = [{"name": "Nigar", "number": "070 808 07 91", "email": "nigarrmustafazada@gmail.com",
             "address": "Baku.7mcr"},
            {"name": "Ceyhun", "number": "055 899 78 98", "email": "aliyevceyhun@gmail.com",
             "address": "Baku.Yasamal"},
            {"name": "Yusif", "number": "050 706 69 96", "email": "yusifzeynalli@gmail.com",
             "address": "Baku.Azadliq"},
            {"name": "Zeynab", "number": "055 478 88 67", "email": "ahmedovazeynab@gmail.com",
             "address": "Baku.Narimanov"},
            {"name": "Gulnaz", "number": "077 591 60 96", "email": "gulnazmammadove@gmail.com",
             "address": "Sumqayit"}]


search_name = tk.Label(window, bg='thistle3', fg="#fff", text="Search name", width=13, height=2).place(x=30, y=60)

search_number = tk.Label(window, bg='thistle3', fg="#fff", text="Search number", width=13, height=2).place(x=30, y=110)

search_name_entry_area = tk.Entry(window, width=30).place(x=140, y=70)

search_number_entry_area = tk.Entry(window, width=30).place(x=140, y=120)


def selected():
    return int(select.curselection()[0])


def select_set():
    for name, number, email, address in contacts:
        select.insert(tk.END, name)
    for cont in contacts:
        select.insert(tk.END, cont['name'])


select_set()


def exit_button():
    window.destroy()


def view_button():
    pass


def reset_button():
    pass


def add_button():
    pass


def delete_button():
    # if search_name_entry_area == dict.keys("name") in nigar_info or yusif_info or ceyhun_info or zeynab_info or gulnaz_info:
    pass


add_button_ = tk.Button(window, bg='thistle2', text="Add", width=10, height=2, command=add_button).place(x=30, y=160)

view_button_ = tk.Button(window, bg='thistle2', text="View", width=10, height=2, command=view_button).place(x=30,
                                                                                                            y=210)

delete_button_ = tk.Button(window, bg='thistle2', text="Delete", width=10, height=2, command=delete_button).place(
    x=30, y=260)

reset_button_ = tk.Button(window, bg='thistle2', text="Reset", width=10, height=2, command=reset_button).place(x=130,
                                                                                                               y=160)

exit_button_ = tk.Button(window, text='Exit', width=8, height=0, bg='brown2', font="arial 12 bold",
                         command=exit_button).place(x=130, y=210)

scroll_bar = tk.Scrollbar(window, orient=tk.VERTICAL)
select = tk.Listbox(window, yscrollcommand=scroll_bar.set, height=17, width=30)
scroll_bar.config(command=select.yview)
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
select.place(x=350, y=70)

window.mainloop()
