# Dictionaryde yashi 18den yuxari olanlarin melumatlari chap edilsin


students = {
    1: {
        'firstname':'Ali',
        'lastname':'Abbasov',
        'subject':'Computer Science',
        'mark': 12,
        'age': 26
    },
    2: {
        'firstname': 'Nigar',
        'lastname':'Movsumova',
        'subject':'Machine Learning',
        'mark': 3.7,
        'age': 26
    }
}

for i in students:
    if students[i]['age'] > 18:
        print(students[i])

