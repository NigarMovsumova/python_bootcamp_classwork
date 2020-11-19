from functools import reduce

# 1. x % 3 == 0
# 2. x - 3
# 3. cemini tap

numbers = [4, 7, 9, 1, 8, 6]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)
#
# product = reduce(lambda a, b: a * b, numbers)
# print(product)
#
# mapped = list(map(lambda x: x - 3, numbers))
# print(mapped)

numbers.reverse()

print(reduce(lambda a, b: a + b, list(map(lambda x: x - 3, list(filter(lambda x: x % 3 == 0, numbers))))))










