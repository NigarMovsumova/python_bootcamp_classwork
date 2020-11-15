from students.FileUtil import load_from_file, write_to_file, truncate_file
from students.GlobalStudents import students

write_to_file(students)
loaded_dictionary = load_from_file()

dictionary_sorted = sorted(students.items(), key=lambda x: (x[1]['age'], x[1]['firstname']), reverse=False)
print(dictionary_sorted)
truncate_file()

write_to_file(dictionary_sorted)
print(load_from_file())
