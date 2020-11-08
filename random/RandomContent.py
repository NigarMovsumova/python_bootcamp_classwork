from random import getrandbits

f = open('random.txt', 'r+')
random_content = f.read()
f.write('123456test')
f.close()

f = open('random.txt', 'r+')
random_content = f.read()
print(random_content)

print('*'*20)

flag = bool(getrandbits(1))
print(flag)

if flag:
    f.truncate(0)
else:
    f.write(random_content)

f.close()

f = open('random.txt', 'r+')
random_content = f.read()
print(random_content)
f.close()

