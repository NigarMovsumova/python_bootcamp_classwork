# Istifadechi 2 reqem daxil edir.
# 1. Vurma
# 2. Bolme
# 3. Difference

try:
    first = float(input('Enter the first number: '))
    second = float(input('Enter the second number: '))
    choice = int(input('''Enter your choice:
    1. Multiply
    2. Divide 
    3. Difference\n'''))
except ValueError as e:
    print(e)

if choice == 1:
    print(first*second)
elif choice == 2:
    try:
        print(first/second)
    except ZeroDivisionError:
        print("Can't divide by zero")
elif choice == 3:
    print(first - second)
else:
    raise BaseException('Test')