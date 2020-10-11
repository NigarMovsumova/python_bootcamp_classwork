uzeyir = 'Uzeyir'
students = [uzeyir, 'Vuqar', 'Ali',
            uzeyir, 'Alpay', 'Kenan',
            'Riad', 'Eldar', 'Behlul',
            'Nigar', 'Nezrin', 'Ilham']
print(students)
print(students[-1])
print(students[1:5])
print(students[:5])
print(students[4:])

students[9] = 'Movsumova'
print(students)

for student in students:
    print(student)

for student in students:
    if student == 'Ilham':
        print('Ilham is in the list')
        break

if 'Ilham' in students:
    print('Ilham is in the list')

print(len(students))

students.append('Shakira')
print(students)

#students.remove('Uzeyir')
#students.remove('Uzeyir')
#students.remove('Uzeyir')
print(students)

students.insert(0, 'Shakira')
print(students)

#students.clear()
#print(students)

students_copy = students.copy()
print(students_copy)

students_duplicate = list(students)
print(students_duplicate)

numbers = [1, 2, 3]
print(students + numbers)


# add all odd numbers to list and print the list

#first = int(input('Enter the first number: '))
#second = int(input('Enter the second number: '))
#odd = []
#even = []

#for number in range(first, second):
#    if number % 2 == 1:
#        odd.append(number)
#    else:
#        even.append(number)

#print(odd)
#print(even)

# istifadechi siyahini ve reqemi daxil edir
# reqem siyahida neche defe rast gelinirse onu tapmaq gerekir
searched_number = int(input('Enter the number to search for: '))
numbers = []
counter = 0

length = int(input('Enter the length of the list: '))
print('Enter the numbers :')
for i in range(0, length):
    number = int(input(''))
    numbers.append(number)
    if number == searched_number:
        counter += 1
print(counter)