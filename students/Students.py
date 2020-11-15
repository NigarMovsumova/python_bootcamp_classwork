import pickle

# file-da ad ve yashlardan ibaret dictionary var
# filedan melumatlari oxuyub, sort edib yeniden,
# evvelki melumatlari silib filedan,
# file-a yazmaq gerekir.
sample = {
    'name': 'Python'
}

file = open("students.txt", "wb")
pickle.dump(sample, file)
file.close()

file = open('students.txt', 'rb')
loaded_dictionary = pickle.load(file)
file.close()

print(loaded_dictionary)



