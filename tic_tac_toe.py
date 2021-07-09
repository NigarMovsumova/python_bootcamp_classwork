from tkinter import *
from tkinter import messagebox
import random as r


# 1. MessageBox duzgun gostermelidir
# 2. resizable olmasin
# 3. O's chance niye ilk once ayrica achilir +
# 4. Kompyuterle oyun (bota qarshi)
# 5. packi evez etmek gridle

def button(frame):
    b = Button(frame, padx=1, bg="white", width=3, text="   ", font=('arial', 60, 'bold'), relief="sunken", bd=10)
    return b


# novbeti oyuncuya kecmek ucun funk
def change_player():
    global a
    for i in ['O', 'X']:
        if not (i == a):
            a = i
            break


def check():
    for i in range(3):
        if b[i][0]["text"] == b[i][1]["text"] == b[i][2]["text"] == a or b[0][i]["text"] == b[1][i]["text"] == b[2][i]["text"] == a:
            messagebox.showinfo("Congrats!!", "'" + a + "' has won")

    if b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] == a or b[0][2]["text"] == b[1][1]["text"] == b[2][0]["text"] == a:
        messagebox.showinfo("Congrats!!", "'" + a + "' has won")

    elif b[0][0]["state"] == b[0][1]["state"] == b[0][2]["state"] == b[1][0]["state"] == b[1][1]["state"] == b[1][2]["state"] == b[2][0]["state"] == b[2][1]["state"] == b[2][2]["state"] == DISABLED:
        messagebox.showinfo(message="No one wins!")


def start_multi_player_mode():
    root = Tk()
    root.title("Tic-Tac-Toe")
    a = r.choice(['O', 'X'])
    # b = [[], [], []]
    for i in range(3):
        for j in range(3):
            b[i].append(button(root))
            b[i][j].config(command=lambda row=i, col=j: click_button(row, col))
            b[i][j].grid(row=i, column=j)

    root.mainloop()


def click_button(row, col):
    b[row][col].config(text=a, state=DISABLED, disabledforeground=colour[a])
    check()
    change_player()
    label = Label()
    label.config(text=a + "'s Chance")
    label.grid(row=3, column=0, columnspan=3)

# def get_text_pc(i, j, gb, l1, l2):
#     global sign
#     if board[i][j] == ' ':
#         if sign % 2 == 0:
#             l1.config(state=DISABLED)
#             l2.config(state=ACTIVE)
#             board[i][j] = "X"
#         else:
#             button[i][j].config(state=ACTIVE)
#             l2.config(state=DISABLED)
#             l1.config(state=ACTIVE)
#             board[i][j] = "O"
#         sign += 1
#         button[i][j].config(text=board[i][j])
#     x = True
#     if winner(board, "X"):
#         gb.destroy()
#         x = False
#         box = messagebox.showinfo("Winner", "Player won the match")
#     elif winner(board, "O"):
#         gb.destroy()
#         x = False
#         box = messagebox.showinfo("Winner", "Computer won the match")
#     elif (isfull()):
#         gb.destroy()
#         x = False
#         box = messagebox.showinfo("Tie Game", "Tie Game")
#     if (x):
#         if sign % 2 != 0:
#             move = pc()
#             button[move[0]][move[1]].config(state=DISABLED)
#             get_text_pc(move[0], move[1], gb, l1, l2)


# def withpc(game_board):
#     game_board.destroy()
#     game_board = Tk()
#     game_board.title("Tic Tac Toe")
#     l1 = Button(game_board, text="Player : X", width=10)
#     l1.grid(row=1, column=1)
#     l2 = Button(game_board, text="Computer : O",
#                 width=10, state=DISABLED)
#
#     l2.grid(row=2, column=1)


# main funk
def play():
    menu = Tk()
    menu.geometry("250x250")
    menu.title("Tic Tac Toe")
    head = Button(menu, text="Welcome to tic-tac-toe",
                  activeforeground='red',
                  activebackground="yellow", bg="red",
                  fg="yellow", width=500, font='summer', bd=5)

    B1 = Button(menu, text="Single Player",
                activeforeground='red',
                activebackground="yellow", bg="red",
                fg="yellow", width=500, font='summer', bd=5)

    B2 = Button(menu, text="Multi Player", activeforeground='red',
                activebackground="yellow", bg="red", fg="yellow",
                width=500, font='summer', bd=5, command=start_multi_player_mode)

    B3 = Button(menu, text="Exit", command=menu.quit, activeforeground='red',
                activebackground="yellow", bg="red", fg="yellow",
                width=500, font='summer', bd=5)
    head.grid()
    B1.pack(side='top')
    B2.pack(side='top')
    B3.pack(side='top')
    menu.mainloop()


# Call main funk
# if __name__ == '__main__':
b = [[], [], []]
a = r.choice(['O', 'X'])
# label = Label(text=a + "'s Chance", font=('arial', 20, 'bold'))
# label.grid(row=3, column=0, columnspan=3)
colour = {'O': "green", 'X': "blue"}
play()