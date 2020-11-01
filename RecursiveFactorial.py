def find_factorial(number):
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result


# 5 * 4 * 3 * 2 * 1 * 1

def find_factorial_recursively(number):
    if number == 0:
        return 1
    return number * find_factorial_with_recursion(number - 1)


print(find_factorial(10000))
print(find_factorial_recursively(5))
# RecursionError: maximum recursion depth exceeded in comparison
print(find_factorial_recursively(10000))
