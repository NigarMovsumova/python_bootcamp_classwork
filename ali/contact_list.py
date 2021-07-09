import tkinter as tk

phone_list = []


# def digit(operation):
#     add.phone_list(operation)

def test():
    print('test button is pressed')


def clear():
    del phone_list


def show_information(operation):
    print(phone_list)


def make_digit_Button(digit):
    return tk.Button(text=digit, bd=5, font=("Arial", 13), fg="gray1", command=lambda: add_digit(digit))


def make_operation_Button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13), command=lambda: add_digit(operation))


win = tk.Tk()
win.geometry(f"540x400")
win["bg"] = "dark green"
win.title("phone book")
calc = tk.Entry(win, justify=tk.RIGHT, font=("Arial", 15), width=15)
calc.insert(0, "0")
make_digit_Button("add").grid(row=2, column=1, stick="wens", padx=10, pady=10)
make_digit_Button("reset").grid(row=2, column=2, stick="wens", padx=10, pady=10)
make_digit_Button("show").grid(row=2, column=3, stick="wens", padx=10, pady=10)
# tk.Entry().grid(row=2, column=4)
button = tk.Button(text="test", command=test)
button.grid(row=2, column=5, stick="wens", padx=10, pady=10)
win.mainloop()

