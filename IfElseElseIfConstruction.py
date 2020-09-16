# 1 reqem daxil edilir
# 1. eger < 0 print "reqem 0dan ashagidir"
# 2. ==0 print ==0
# 3. > 0 print >0


#first_number = float(input('Enter the first number: '))

#if first_number < 0:
#    print("reqem 0dan ashagidir")
#elif first_number == 0:
#    print('reqem 0a beraberdir')
#else:
#    print("reqem 0dan yuxaridir")


# ishiqfor
# 3 rengi - qirmizi, sari, yashil
# qirmizi - 'Dur'
# sari - 'Gozle'
#yashil - 'Yol senindir'

stoplight_color = int(input('''Ishiqfor rengini daxil edin:
1. Qirmizi
2. Yashil
3. Sari\n'''))

if stoplight_color == 1:
    print('Dur')
elif stoplight_color == 2:
    print('Gozle')
elif stoplight_color == 3:
    print('Sari')
else:
    print('Sehv sechim etmisiniz.')
