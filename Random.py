import random as r

mylist = ["Tony", "Habib", "McGregor"]

list = r.choices(mylist, weights=None, k=5)
print(list)

print(r.choices(mylist, weights=None, k=14))

numbers_list = r.choices(range(0, 1), weights=None, k=15)
numbers_list = r.choices([0], weights=None, k=15)

print(numbers_list)
