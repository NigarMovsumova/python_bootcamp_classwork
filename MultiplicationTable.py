# MultiplicationTable

# 1. İstifadəçi diapozonu daxil edir və
# proqram həmin diapozonda vurma cədvəlini konsola çıxarır.
# Məsələn, əgər istifadəçi 3 və 5 daxil edərsə, bu formada çap edilməlidir.
# 3*1 = 3 3*2 = 6 3 * 3 = 9 ... 3 * 10 = 30
# 5*1 = 5 5 *2 = 10 5 * 3 = 15 ... 5 * 10 = 50
# 5

for j in range(3, 6):
    print('\n')
    for i in range(1, 11):
        print(j, ' * ', i, ' = ', 5 * i, end='  ')
