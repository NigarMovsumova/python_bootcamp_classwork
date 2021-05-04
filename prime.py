# Eger eded sadedirse True,
# murekkebdirse False chap edin.

number = int(input('Enter the number: '))
# boolean - True, False
is_prime = True
for i in range(2, number):
    if number % i == 0:
        is_prime = False
        print(number, 'tam bölünür', i, 'ədədinə' )
        break
print(number, 'sadedir ?', is_prime)

