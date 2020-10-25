# [3, 4, 5, 15, 17, 25, ...]
# 12000000, 10000, 1200, 3450000

# 0 - 120
# []

# 0, 1, 2, 3, 4, 5
# [3, 4, 5, 15, 17, 25]

population_age = [0, 1, 2, 2, 2, 2, 3, 4, 4]
age_statistics = [0, 0, 0, 0, 0]
for age in population_age:
    age_statistics[age] += 1
print(age_statistics)

# 2 * height * length + 2 * height * width
