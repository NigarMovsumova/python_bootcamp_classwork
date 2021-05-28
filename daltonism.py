# Tkinter vasitəsilə daltonizmi yoxlayan tədbiq yazmaq gərəkir
# Istifadechiye 4 defe muxtelif rengler gosterilir (Label)
# ve ashagida 4 muxtelif variant verilir(Button) her defesinde
# Onlarin arasinda 1 duz ve 3 sehv variantlar olur.
# Istifadechi duzgun cavablar verdikce, onlari hesablamaq gerekir.
# Eger 4 sualin 4ude duzdurse, daltonik olmadigi qeyd
# olunmalidir sonucda.
# Eger 3 duzdurse, daltonizm elametleri oldugu qeyd olunmalidir.
# Eger 0, 1 ve ya 2 duz cavab veribse, daltonik oldugu
# qeyd olunmalidir.
from tkinter import *


def check_answer(user_answer, correct_answer):
    print(user_answer, '  ', correct_answer)
    if user_answer == correct_answer:
        print('Answer is correct')
    else:
        print('Answer is not correct')


root_window = Tk()
root_window.title('Game App')
root_window.geometry('500x500')
# fg = foreground color
# bg = background color
label = Label(text='', bg='black', height=3, width=50)
label.pack()

red_button = Button(text='Red', width=50, height=1, command=
                    lambda: check_answer('red', label.cget("bg")))
red_button.pack()

green_button = Button(text='Green', width=50, height=1,
                      command=lambda: check_answer('green', label.cget("bg")))
green_button.pack()

black_button = Button(text='Black', width=50, height=1,
                      command=lambda: check_answer('black', label.cget("bg")))
black_button.pack()

root_window.mainloop()



