# 2. 1den 100e kimi 2ye bolunenlerin sayini tapmaq gerekir

# count = 0
# for i in range(1, 20):
#     if i % 2 == 0:
#         # s = s + 1
#         count += 1
# print(count)

# 1. 1-den 100e kimi ededler var, onlarin cemini
# tapmaq lazimdir, cemi 100den ashagi olana kimi.

# 20-den 100e kimi ededler var, onlarin hasilini
# tapmaq gerekir, ededler 13e bolunmeyene kimi.
product = 1
for i in range(20, 30):
    if i % 13 == 0:
        break
    product *= i
print(product)


