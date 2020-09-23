#annual_fee = float(input('Enter the university annual fee: '))
#print(annual_fee)

try:
    annual_fee = float(input('Enter the university annual fee: '))
except Exception as e:
    print(e, 'Your input is not correct. Quack-quack.')
else:
    print('Else code block')
finally:
    print('Finally code block')
