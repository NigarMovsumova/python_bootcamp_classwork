# 1-10 arası ədədləri çap edin.

# for i in range(1, 11):
#     print(i)

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# n reqemli ededin reqemlerini chap edin
number = int(input('Enter the number: '))
counter = 0
while number != 0:
    # print(number % 10)
    number = number // 10
    counter += 1
print(counter)

# n reqemli ededin yalniz cut reqemlerini cemleyin
