def my_decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper


def say_hello():
    print("Hello")

# 1. How are you ? yazan funksiya elave edin
# 2. o funksiyani istifade edin
# 3. print(before) ve print(after) yerine 2 bashqa hansisa funksiya
# chagirin, hansilar ki, Hi ve Good Bye

# Hi
# How are you ?
# Good bye


say_hi = my_decorator(say_hello)
say_hi()



