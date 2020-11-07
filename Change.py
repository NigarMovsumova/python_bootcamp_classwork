# 10. İstifadəçi sahib olduğu pulu daxil edir
# (Kəsr halda: məsələn 15.30). İstifadəçinin
# neçə manat və neçə qəpiyi olduğunu ekrana çıxarın.
# ( Ekrana 15 manat, 30 qəpik çıxmalıdır)

money_amount = float(input('Enter your money amount: '))
print('{} manat, {} qepik'.format(
    int(money_amount),
    int(money_amount * 100 - int(money_amount) * 100)))
