import random

print(random.randrange(1, 10))
print(random.randrange(1, 10, 2))
print(random.randrange(0, 101, 10))

print(random.random())
print(random.uniform(1, 10))
#
string_samples = ['one', 'eleven', 'twelve', 'five', 'six', 'ten']

sample = random.sample(string_samples, 6)
print('random sample:', sample)