# import tkinter

# from tkinter import *

# import tkinter as tk

# numpy, pandas -> np, ps

from core.basket import test_imports, Basket
from tkinter import Tk


def testing_app():
    print('testing imports from app.py')


root_window = Tk()
test_imports()
basket = Basket()
print(basket)
root_window.mainloop()

