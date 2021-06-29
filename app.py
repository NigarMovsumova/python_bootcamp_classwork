

choice = int(input('''Enter your choice:
1. Show todo list
2. Remove from list
3. Add to the list
4. Quit the proqram\n'''))
while choice != 4:
    if choice == 1:
        print('Show todo list')
    elif choice == 2:
        print('Remove from list')
    elif choice == 3:
        print('Add to the list')
    else:
        print('Wrong choice.')
    choice = int(input('''Enter your choice:
    1. Show todo list
    2. Remove from list
    3. Add to the list
    4. Quit the proqram\n'''))

print('Good Luck!!!')