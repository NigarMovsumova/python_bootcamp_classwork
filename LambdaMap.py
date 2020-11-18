from functools import reduce

numbers = [4, 7, 9, 1, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

product = reduce(lambda a, b: a * b, numbers)
print(product)

mapped = list(map(lambda x: x - 3, numbers))
print(mapped)

# 1. x % 3 == 0
# 2. x - 3
# 3. cemini tap









