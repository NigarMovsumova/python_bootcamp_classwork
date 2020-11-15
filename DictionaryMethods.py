
subjects = {
    'humanitarian': ['Literature', 'Psychology', 'Language', 'History'],
    'STEM': ['Physics', 'Computer Science', 'Chemistry', 'Math'],
    'test': ['test'],
    # 'test': ['test1'],
    # 'test':['test2']
}

for subject in subjects:
    print(subject, subjects[subject])

# subjects.clear()
# print(len(subjects))


# subjects.pop('test')
# subjects.pop('humanitarian')
# subjects.pop('STEM')

# subjects.popitem()

# for subject in subjects:
#     print(subject, subjects[subject])

# del subjects['test']
#
# for subject in subjects:
#     print(subject, subjects[subject])

subjects_copy = subjects.copy()
print(subjects_copy)

subjects['test'] = 'Nigar'
print(subjects)
print(subjects_copy)

subjects_incorrect_copy = subjects
subjects['test'] = 'Nigar'

print(subjects)
print(subjects_incorrect_copy)


