def isPowerOf2(number, power):
    if number == 1:
        return 0
    number /= 2
    if number == 2:
        return power + 1
    elif number > 2:
        return isPowerOf2(number, power + 1)
    else:
        return None


# isPowerOf2 -> number = 8, power = 1
# 8 / 2 = 4 - number
# isPowerOf2(4, 2) power = 2
# 4 / 2 = 2 - number
# return power + 1 = 3

power = 1
print(isPowerOf2(6, power))
print(isPowerOf2(8, power))
print(isPowerOf2(32, power))
print(isPowerOf2(1, power))
print(isPowerOf2(64, power))
print(isPowerOf2(1, power))
