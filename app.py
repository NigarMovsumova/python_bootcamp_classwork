from todo_list import show_list, add_task, delete_task
# import todo_list as tl
# import todo_list
# from todo_list import *

choice = input('''Enter your choice:
1. Show todo list
2. Remove from list
3. Add to the list
4. Quit the proqram\n''')
while choice != '4':
    if choice == '1':
        show_list()
    elif choice == '2':
        delete_task()
    elif choice == '3':
        add_task()
    else:
        print('Wrong choice.')
    choice = input('''Enter your choice:
    1. Show todo list
    2. Remove from list
    3. Add to the list
    4. Quit the proqram\n''')

print('Good Luck!!!')