import pickle

capitals = {'Azerbaijan': 'Baku',
           'United Kingdom': 'London',
           'Germany': 'Berlin',
           'Goranboy': 'Gulustan'
           }

print(capitals['Azerbaijan'])
print(capitals['Goranboy'])

pickled_capitals = pickle.dumps(capitals)
loads = pickle.loads(pickled_capitals)

print(pickled_capitals)
print('*'*20)
print(loads)

file = open('pickle.txt', 'wb')

pickle.dump(capitals, file)

file.close()
