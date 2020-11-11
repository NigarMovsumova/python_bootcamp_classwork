tuple_example = (1, 2, 3)
empty_tuple = ()

print(tuple_example)
print(empty_tuple)

# TypeError: 'tuple' object does not support item assignment
#empty_tuple[0] = 5
#tuple_example[0] = 5
#print(empty_tuple)
#print(tuple_example)

# TypeError: can only concatenate tuple (not "int") to tuple
# tuple_example += 5
# print(tuple_example)

tuple_example += (5 * 5,)
print(tuple_example)

print(tuple_example[0])

# NameError: name 'tuple_example' is not defined
# del tuple_example
# print(tuple_example)

print(len(tuple_example))

for i in range(0, len(tuple_example)):
    print(tuple_example[i])

print(('Hello!',) * 4)
print('*'*4)

print(5 in tuple_example)
print(25 in tuple_example)

# (1, 2, 3, 25)
# print(tuple_example[1:])
# print(tuple_example[:1])
print(tuple_example[-1:-2])
print(tuple_example[-2:-1])
print(tuple_example[-2:])
print(tuple_example[0:2])
print(max(tuple_example))
print(min(tuple_example))

print(tuple(['Nigar', 26]))
print(list(('Nigar', 26)))





