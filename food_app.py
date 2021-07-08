from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry('350x500')
window.title("wolt v1.0.0")
window.resizable(0, 0)

r = 0
j = 0

for i in range(100):
    c = str(5000+r)
    Frame(window, width=10, height=500, bg='#FF' + c).place(x=j, y=0)
    j = j+10
    r = r+1

Frame(window, width=250, height=400, bg='#FFFFFF').place(x=50, y=50)


#Label

l1 = Label(window,text="Username", bg='white')
l = ('consolas',13) # right here, we are using tuple which contains two parametr, one of thoso is writing style (str), the other one is size (int).
l1.config(font=l)
l1.place(x=80, y=200)

l2 = Label(window,text="Password", bg='white')
l2.config(font=l)
l2.place(x=80,y=280)

l3 = Label(window,text="W O L T", bg='white',fg='#FF4000')
l2 = ('consolas', 25)
l3.config(font=l2)
l3.place(x=110, y=110)

e1 = Entry(window,width=20, border=0)
e1.config(font=l)
e1.place(x=80, y=230)

e2 = Entry(window,width=20,border=0)
e2.config(font=l)
e2.place(x=80, y=310)

Frame(window, width=180, height=2, bg='#141414').place(x=80, y=250)
Frame(window, width=180, height=2, bg='#141414').place(x=80, y=330)


def cmd():
    if e1.get() =='admin1' and e2.get() == "admin1234":
        window.destroy()
        q = Tk()
        q.title("H O M E")
        q.geometry('500x500')
        q.resizable(0, 0)
        r = 0
        j = 0
        for i in range(100):
            c = str(5000 + r)
            Frame(q, width=10, height=500, bg='#FF' + c).place(x=j, y=0)
            j = j + 10
            r = r + 1
        def MenuCmd():
            top = Tk()
            sb = Scrollbar(top)
            sb.winfo_geometry('300x300')
            sb.pack(side=RIGHT, fill=Y)

            mylist = Listbox(top, yscrollcommand=sb.set)


            mylist.insert(END, "Number  1" )

            mylist.pack(side=LEFT)
            sb.config(command=mylist.yview)

            mainloop()
        orderButton = Button(q, text="M E N U", width=20, height=5, bg='white', fg='#FF4000', border=0,command=MenuCmd).place(x=80, y=200)
        l1 = Label(q, text="W O L T", bg='white', fg='#FF4000')
        l = ('consolas', 30)
        l1.config(font=l)
        l1.place(x=160, y=50)
        q.mainloop()
    else:
        messagebox.showinfo("Login Failed!", "   Plese check username and password again.    ")


button1 = Button(window, text="L O G I N", width=15, height=2, bg='#FF4000', fg='white', command=cmd, border=0).place(x=115,y=370)

window.mainloop()

