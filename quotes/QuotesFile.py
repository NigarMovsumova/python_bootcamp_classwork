f = open('quotes.txt', 'r+')
quotes = f.read()
print(quotes)

for i in range(3):
    f.write('\nnew line' + str(i))

print(quotes)

f = open('quotes.txt', 'r+')
quotes = f.read()
print(quotes)
