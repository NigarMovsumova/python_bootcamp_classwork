try:
    int(input('Test: '))
except ValueError:
    print('except ValueError')
else:
    pass
finally:
    print('finally block')