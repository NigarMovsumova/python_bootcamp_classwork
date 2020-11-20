from random import randint


def random_numbers():
    random_numbers = []
    isPositive = False
    sum = 0
    for i in range(10):
        random_number = randint(-30, 20)
        random_numbers.append(random_number)
        if random_number > 0:
            isPositive = True
        if isPositive:
            sum += random_number
    print(random_numbers)
    return sum


numbers = random_numbers()
print(numbers)
