# 1-100 araliq. 2, 3, 5, 7ye ayriliqda bolunen
# ededlerin cemini hesablamaq gerekir.

i = 1
count = 0
numbers_sum = 0
while i <= 11:
    i += 1
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        count += 1
        numbers_sum += i
print(count)
print(numbers_sum)