students = ['Rena', 'Nigar', 'Nigar', 'Nuray', 'Nigar',
            'Shakhhuseyn', 'Yusif', 'Murad',
            'Seymur', 'Zamin', 'Sabuhi',
            'Elmar']

# for student in students:
#     print(student)

# print(students[-1])
# print(students[0])
# text = 'test text'
# print(text[0])
# print(text[4])
# print(text[0])
# print(students[0:4])
# print(students[-5:-1])
# print(students[-5:])
# print(students[4:])
# print(len(students))
# students.append('Lidiya')
# students.append('Farize')
# students.append('Cume')
# students.append('Nelbeki')
# students.append('Tukezban')
# print(students)

# Siyahı verilir. Siyahıda x elementi var.
# Həmin elementi istifadechinin daxil etdiyi
# sətrlə əvəz edin.

characters = ['word', 'x', 'x', 'x', 'x']
# test_input = input('Enter the word to replace with:')
# index = 0
# counter = 0
# for character in characters:
#     if character == 'x':
#         counter += 1
#         characters[index] = test_input
#     if counter == 2:
#         break
#     index += 1
#
# print(characters)

print('t' in 'table')
print('Elmar' in students)
print('Sabina' in students)
print(len(students))
students.remove('Nigar')
print(students)
students.insert(7, 'Baxtiyar')
print(students)
# students.append(77)
# students.append(True)
# students.append(7.876)
print(students)
index = 0

numbers = [77, 777, 7]
students += numbers
students = students + numbers
print(students + numbers)
print(students)