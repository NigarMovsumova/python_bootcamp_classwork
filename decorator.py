# 1. Decorator yazmaq gerekir.
# Dekoratordan kenar istifadechi reqemi daxil edir
# Dekorator yoxlayir ki, hemin reqem int, floatdir mi.
# eger intdirse, o zaman 2ye vurub, **2 tapsin.
# floatdirsa, kesrnen tam hissesini toplasin.


def sample_decorator(num):

    def int_calculation(num):
        return (num * 2) ** 2

    def sum_number_parts(num):
        return int(num) + (num - int(num)) * 10 ** (len(str(num))-2)

    # print(num % 1)
    if num % 1 == 0.0:
        return int_calculation(num)
    else:
        return sum_number_parts(num)


number = float(input('Enter the number:'))
print(sample_decorator(number))
