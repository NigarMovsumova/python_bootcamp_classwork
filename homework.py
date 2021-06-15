students = {
    "Nigar": 90,
    "Ali": 95
}

choice = int(input('''
Enter your choice:
1. Add a student'''))

if choice == 1:
    name = input('Enter new student\'s name: ')
    mark = int(input('Enter student\'s mark: '))
    students[name] = mark
    print('Student is added.')

print(students)
