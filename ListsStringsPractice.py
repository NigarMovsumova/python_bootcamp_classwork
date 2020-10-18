cars = ['BMW', 'Rolls Royce', 'Bentley', 'Kamaz', 'Lada Kalina', 'Tesla']
scores = [4.3, 4.7, 4.8, 2.3, -1.6, 5]

# BMW - 4.3
# Rolls Royce - 4.7
# Bentley - 4.8
# Tesla - 5

# 1. eger 4den yuxaridirsa ve ya beraberdirse score,
# mashin adi + meslehetli oldugu qeyd olunsun
# 2. eger neqativdirse, - tehlukelidir
# 3. eger 0 - 4 arasindadirsa - meslehet deyil.

i = 0
for i in range(0, 4):
    print(cars[i], scores[i])
    print(cars[i], '-', scores[i])
    print(cars[i], '-', scores[i], sep="")
    print('{}-{}'.format(cars[i], scores[i]))
    print(cars[i], scores[i], sep='-')

i = 0
for i in range(0, len(scores)):
    if scores[i] >= 4.8:
        print(cars[i])

# 1. eger 4den yuxaridirsa ve ya beraberdirse score,
# mashin adi + meslehetli oldugu qeyd olunsun
# 2. eger neqativdirse, - tehlukelidir
# 3. eger 0 - 4 arasindadirsa - meslehet deyil.

i = 0
for i in range(0, len(scores)):
    if scores[i] <= 0:
        print(cars[i], ' is dangerous')
    elif scores[i] >= 4:
        print(cars[i], ' is secure')
    else:
        print(cars[i], 'is not recommended')
