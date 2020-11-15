import pickle

students = {
    1: {
        'firstname': 'Ali',
        'lastname': 'Abbasov',
        'subject': 'Computer Science',
        'mark': 12,
        'age': 26
    },
    2: {
        'firstname': 'Aysha',
        'lastname': 'Movsumova',
        'subject': 'Machine Learning',
        'mark': 3.7,
        'age': 17
    },
    3: {
        'firstname': 'Nigar',
        'lastname': 'Movsumova',
        'subject': 'Machine Learning',
        'mark': 3.7,
        'age': 39
    }
}


def write_to_file(dictionary, filename='students.txt'):
    file = open(filename, "wb")
    pickle.dump(dictionary, file)
    file.close()


def load_from_file(filename='students.txt'):
    file = open(filename, 'rb')
    loaded_dictionary = pickle.load(file)
    file.close()
    return loaded_dictionary


def truncate_file(filename='students.txt'):
    file = open(filename, 'wb')
    file.truncate()
    file.close()
