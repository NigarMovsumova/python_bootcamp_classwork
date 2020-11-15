import pickle

# file-da ad ve yashlardan ibaret dictionary var
# filedan melumatlari oxuyub, sort edib yeniden,
# evvelki melumatlari silib filedan,
# file-a yazmaq gerekir.


students = {
    1: {
        'firstname': 'Ali',
        'lastname': 'Abbasov',
        'subject': 'Computer Science',
        'mark': 12,
        'age': 17
    },
    2: {
        'firstname': 'Aysha',
        'lastname': 'Movsumova',
        'subject': 'Machine Learning',
        'mark': 3.7,
        'age': 15
    },
    3: {
        'firstname': 'Nigar',
        'lastname': 'Movsumova',
        'subject': 'Machine Learning',
        'mark': 3.7,
        'age': 17
    }
}

file = open("students.txt", "wb")
pickle.dump(students, file)
file.close()

file = open('students.txt', 'rb')
loaded_dictionary = pickle.load(file)
file.close()

dictionary_sorted = sorted(students.items(), key=lambda x: (x[1]['age']), reverse=True)

print(dictionary_sorted)

file = open('students.txt', 'wb')
file.truncate()
file.close()

# file = open('students.txt', 'rb')
# file_content = pickle.load(file)
# print(file_content)
# file.close()

file = open('students.txt', 'wb')
pickle.dump(dictionary_sorted, file)
file.close()

file = open('students.txt', 'rb')
print(pickle.load(file))
file.close()
