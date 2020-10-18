list = ['Riad', 'Sarkhan', 'Orkhan', 'Uzeyir']

# RiadSarkhan
# SarkhanOrkhan
# OrkhanUzeyir
# Uzeyir

print(list[0])
print(len(list))
print(len(list[0:2]))
print(list[1:])

list[1] = 'Behlul'
print(list)

i = 0
for x in list:
    print(x, ' ', i)
    i += 1

i = 0
while i < len(list):
    print(list[i], ' ', i)
    i += 1

for i in list:
    print(i)

for i in list:
    print(i[0])

for i in list:
    print(i[-1])

print('\n')

list = ['BMW', 'Alpha Romeo', 'Jaguar', 'Bentley']

i = 0
for i in range(0, len(list) - 1):
    print(list[i], list[i + 1], sep='')
print(list[-1])

for i in range(0, len(list) - 1):
    print('{first}{second}'.format(second=list[i + 1], first=list[i]))
