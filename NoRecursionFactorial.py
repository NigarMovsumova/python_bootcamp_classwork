def factorial():
    number = int(input("Enter the number:"))
    factorial = 1
    for i in range(2, number + 1):
        factorial *= i
    print(factorial)


