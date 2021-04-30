# 1-100 araliginda yalniz cut reqemlerin cemini
# tapmaq gerekir.

numbers_sum = 0
for i in range(1, 100):
    if i % 2 == 0:
        numbers_sum = numbers_sum + i
print(numbers_sum)