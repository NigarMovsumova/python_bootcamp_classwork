import pickle
original = {'Illinois': 'Aurora', 'Massachusetts': 'Boston', 'Florida': 'Orlando'}
pickled = pickle.dumps(original)
identical = pickle.loads(pickled)
print('Original: ', original, '\nPicked: ', pickled, '\nIdentical: ', identical)
