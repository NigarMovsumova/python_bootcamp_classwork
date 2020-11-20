import pickle
f = open('order.txt', 'rb')
a = pickle.load(f)
print(a)
f.close()