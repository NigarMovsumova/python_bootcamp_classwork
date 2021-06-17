students = {"Kazimov Seymur Aydin",
            "Suleymanov Murad Tahir",
            "Ehmedov Sebuhi Yalhcin"}
fullname = input("Enter the name:")
flag = True
for student in students:
    if student.split(" ")[0] == fullname.split(" ")[0]:
        print('Student is in already in the list.')
        flag = False
        break

if flag:
    students.add(fullname)
    print('Student is added.')
    print(students)

