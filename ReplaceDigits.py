# 2. İstifadəçi istənilən tam rəqəmi daxil edir. O ədəddən bütün 3 və 6 rəqəmlərini silib, konsola çıxartmaq gərəkir.

try:
    number = int(input('Enter a number:'))
    print(str(number).replace("3", "").replace("6", ""))
except ValueError:
    print("Your input is not correct. Please try again.")
