students = []
# name surname group_name gender age score speciality
student1 = ["tural", "Eliyev", "group_az_123", "male", 21, 76.5, "Programming"]
student2 = ["ali", "Memmedov", "group_az_234", "male", 25, 100, "IT"]
student3 = ["leyla", "Eliyeva", "group_az_450", "female", 21, 98.5, "IT"]
student4 = ["tural", "Eliyev", "group_az_123", "male", 18, 76.5, "Programming"]
student5 = ["nergiz", "Orucova", "group_az_450", "male", 20, 76.3, "IT"]
student6 = ["elshen", "Memmedli", "group_az_234", "female", 27, 89.2, "Design"]
student7 = ["ramiz", "Quliyev", "group_az_450", "male", 16, 76.5, "Design"]
student8 = [
    "aygun", "Semedova", "group_az_234", "female", 29, 90.5, "Programming"
]
student9 = ["murad", "Eliyev", "group_az_234", "male", 28, 76.1, "IT"]
student10 = [
    "nadir", "Nadirli", "group_az_123", "male", 32, 76.5, "Programming"]

students.append(student1)
students.append(student2)
students.append(student3)
students.append(student4)
students.append(student5)
students.append(student6)
students.append(student7)
students.append(student8)
students.append(student9)
students.append(student10)

for i in range(len(students)):
    if students[i][6] == 'Programming' and students[i][4] > 23:
        print(students[i])

print('*' * 6)
for i in range(len(students)):
    if students[i][0][0] in ['a', 'A']:
        print(students[i])

print('*' * 6)
for i in range(len(students)):
    if students[i][3] == 'female':
        print(students[i])

print('*' * 6)
for i in range(len(students)):
    students[i][5] = students[i][5] - 10
    students[i][0] = students[i][0].capitalize()
    students[i][2] = students[i][2].upper()

for i in students:
    print(i)
