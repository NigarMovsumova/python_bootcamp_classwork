# 1. Qirmizi - Dur
# 2. Yashil - Kech
# 3. Sari - Gozle

stoplight_color = int(input('''Enter the stoplight color:
1. Red
2. Green
3. Yellow \n'''))
if stoplight_color == 1:
    print('Stop')
elif stoplight_color == 2:
    print('Go')
elif stoplight_color == 3:
    print('Get ready')
else:
    print('Your input is invalid. No such stoplight color.')
