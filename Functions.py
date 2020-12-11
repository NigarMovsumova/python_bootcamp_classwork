def say_hello(name):
    return f"Hello {name}"
    #return "Hello {}".format(name)


def say_hi(name):
    return f'Hi, {name}'


def greet_bob(greeter_func):
    return greeter_func("Bob")


def greet_ted(greeter):
    return greeter('Ted')


print(greet_bob(say_hello))
print(greet_bob(say_hi))
print(greet_ted(say_hello))
print(greet_ted(say_hi))
