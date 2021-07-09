import tkinter as tk

window = tk.Tk()
window.title('Phone book')
window.geometry('600x500')
window.configure(bg='PaleTurquoise2')
window.attributes('-alpha', 0.9)
dates = []
update_book = []

# Add Information
# def add():
#     global datas
#     datas.append([search_name_entry_area.get(), search_number_entry_area.get(), (1.0, "end-1c")])
#     update_book()
#
#
# def update_book():
#     select.delete(0, tk.END)
#
# def view():
#     search_name_entry_area.set(datas[int(select.curselection()[0])][0])
#     search_number_entry_area.set(datas[int(select.curselection()[0])][1])

# for n, p, a in datas:
#     select.insert(tk.END, n)
# b2 = tk.Button(window, text= 'Show numbers',  width=15, height=2, command=show_numbers)
# b2.pack()
search_name = tk.Label(window, bg='thistle3', fg="#fff", text="Search name", width=13, height=2).place(x=30, y=60)

search_number = tk.Label(window, bg='thistle3', fg="#fff", text="Search number", width=13, height=2).place(x=30, y=110)

search_name_entry_area = tk.Entry(window, width=30).place(x=140, y=70)

search_number_entry_area = tk.Entry(window, width=30).place(x=140, y=120)


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

view_button_ = tk.Button(window, bg='thistle2', text="View", width=10, height=2, command=view_button).place(x=30, y=210)

delete_button_ = tk.Button(window, bg='thistle2', text="Delete", width=10, height=2, command=delete_button).place(x=30,
                                                                                                                  y=260)

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
