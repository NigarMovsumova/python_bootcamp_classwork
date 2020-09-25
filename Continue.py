# for / while
first = int(input('Enter the first number:'))
second = int(input('Enter the second number:'))

for x in range(first, second):
    if x % 5 == 0:
        print(x)
    else:
        continue