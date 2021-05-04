# 15) İstifadəçi 5 rəqəmli ədəd daxil edir,
# ədədi əksinə çevirən proqram yazın. - for

# % 10
# // 10
# number = 9876
# reversed_number = 6789
# print(976 % 10)
# print(976 // 10)

# print(number % 10)
# number = number // 10
# print(number)
#
# print(number % 10)
# number = number // 10
# print(number)
#
# print(number % 10)
# number = number // 10
# print(number)

# print('hello' + 'world')
# print('6' + '7' + '8' + '9')
# konkatenasiya
# concatenation
# concat
number = int(input('Enter the number: '))
# reversed_number = ""
# for i in range(0, 4):
#     reversed_number = reversed_number + str(number % 10)
#     number = number // 10
#
# print(reversed_number)

reversed_number = 0
for i in range(0, 4):
    reversed_number = reversed_number * 10 + number % 10
    number = number // 10
print(reversed_number)
# 9876
# reversed_number = 6
# 987
# reversed_number = 60 + 7 = 67
# 98
# reversed_number = 670 + 8 = 678
# 9
# reversed_number = 6780 + 9
