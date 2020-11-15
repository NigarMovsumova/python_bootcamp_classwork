write_to_file(students)
loaded_dictionary = load_from_file()

dictionary_sorted = sorted(students.items(), key=lambda x: (x[1]['age']), reverse=False)
print(dictionary_sorted)
truncate_file()

write_to_file(dictionary_sorted)
print(load_from_file())
