# 1. filedan melumati oxuyursunuz
# 2. eger reqeme cevire bilirsinizse, info-da gosterirsiniz reqemi
# 3. eger reqeme cevirmek olmursa, error sheklinde gosterirsiniz

from tkinter import messagebox

sample_file = open('messagebox.txt', 'r')
file_content = sample_file.read()

try:
    messagebox.showinfo(int(file_content))
except ValueError:
    messagebox.showerror(file_content, 'can not be converted to int')

