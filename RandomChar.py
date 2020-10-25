# 1. random 2 herf goturursunuz
# 2. onlarin ASCII tableda olan kodunu proqramin ichinde teyin edirsiniz
# 3. cemini tapirsiniz hemin kodlarin
# 4. ve cemine uygun ASCIIde simvol varsa, chixarirsiniz
# 5. yoxdursa, chap edirsiniz ki, bu indeksde simvol yoxdur ASCII tableda.
import random

list = ['1', ' ', '', '\b', '2', 'u']

first_char = ord(random.choices(list)[0])
second_char = ord(random.choices(list)[0])
print(first_char)
print(second_char)

if first_char + second_char < 128:
    print(chr(first_char + second_char))
else:
    print('This char is not in ASCII table')
