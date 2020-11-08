f = open('../test.txt')
dino = f.read()
print(dino)
f.close()

f = open('../test.txt', 'r')
while True:
    dino = f.read(1024)
    print(dino)
    if not dino:
        break
f.close()

f = open('../test.txt', 'a+')
for i in range(3):
 f.write('\nnew line' + str(i))
f.close()

f = open('../test.txt')
dino = f.read()
print(dino)
f.close()

