# Funksiya aşağı və yuxarı həddləri qəbul edir.
# Həddlər istifadəçi tərəfindən daxil edilməlidir.
# Həmin aralıqda olan rəqəmləri çap etmək gərəkir.
# Heçnə qaytarmağa ehtiyac yoxdur funksiyadan.


def print_numbers(minimum, maximum):
    for i in range(minimum, maximum + 1):
        print(i)


minimum = int(input('Enter the lower limit: '))
maximum = int(input('Enter the higher limit: '))
print_numbers(minimum, maximum)
