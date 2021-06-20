# 6. İstifadəçi sahib olduğu pulu daxil edir
# (Kəsr halda: məsələn 15.30).
# İstifadəçinin neçə manat və neçə qəpiyi olduğunu ekrana çıxarın.

money_amount = float(input('Enter the money amount you have: '))
print(int(money_amount))
print(money_amount % 1 * 100)
