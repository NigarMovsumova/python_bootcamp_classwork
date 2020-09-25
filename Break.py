# for / while
first = int(input('Enter the first number:'))
second = int(input('Enter the second number:'))

for x in range(first, second):
    if x % 5 == 0:
        print(x)
        break

# Istifadechi araliq daxil edir.
# O araliqda sonu 9la bitirse reqem, ekrana chixarmaginiz gerekir 1-ni (ilk 2-sini)

count = 0

for x in range(first, second):
    if x % 10 == 9:
        count += 1
        print(x)
    if count >= 2:
        break

count = 0
x = first
while x < second:
    if x % 10 == 9:
        count += 1
        print(x)
    if count >= 2:
        break