# factorial - 5! = 1 * 2 * 3 * 4 * 5

def calculate_factorial(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial


def calculate_factorial_recursively(n, result):
    if n == 1 or n == 0:
        return result
    result = result * n
    return calculate_factorial_recursively(n-1, result)


print(calculate_factorial(5))
print(calculate_factorial(0))
print(calculate_factorial(1))
print(calculate_factorial_recursively(5, 1))
print(calculate_factorial_recursively(0, 1))
print(calculate_factorial_recursively(1, 1))
number = int(input('Enter your number:'))
print(calculate_factorial_recursively(number, 1))
