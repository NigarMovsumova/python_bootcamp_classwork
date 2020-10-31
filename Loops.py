low = int(input('Enter the lower limit:'))
high = int(input('Enter the higher limit:'))

sum = 0
product = 1

for i in range(low, high + 1):
    if i % 2 == 0:
        sum += i
    else:
        product *= i

print('The sum of even numbers = {},\nthe product of odd numbers = {}'.format(sum, product))
