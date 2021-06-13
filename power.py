def is_power_of_2(number):
    if number == 1.0:
        print(True)
        return
    if number % 1 != 0.0:
        print(False)
        return
    is_power_of_2(number/2)


number = int(input("Enter the number:"))
is_power_of_2(number)
