print('hello world')
print('hello world'[1])
print(len('hello world'))
alpay1 = 'Alpay, haqqini halal ele'
#print(alpay1[0:5:2])
print(alpay1[-4:-1])
step = '      Step Computer Akademiyasi     '
step_stripped = step.strip()
print(step)
print(step_stripped)
print(step_stripped.lower())
print(step_stripped.upper())
print(step_stripped.replace('e', '*'))
print(step_stripped.replace('e', ' '))
blm = 'black lives matter'
print(blm.strip(','))
print('black' in blm)
print('black' not in blm)

#1. dovr setrin axrindan evvele gedir
#2. 5 simvol upper
#3. 5 simvol lower
#4. araliqlar silinmelidir boyurlerde +
#5. j evez olunmalidir _+

lorem = '     LJREM ijsum     '
print(lorem)
lorem = lorem.strip()
lorem = lorem.replace('J', '_')
lorem = lorem.replace('j', '_')
print(lorem)

i = len(lorem) - 1
while i >= 0:
    if i >= len(lorem) - 5:
        print(lorem[i].upper())
    elif i >= len(lorem) - 10:
        print(lorem[i].lower())
    i -= 1
