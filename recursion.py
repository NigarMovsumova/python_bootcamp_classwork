def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n-1)


def sum_recursive(current_number, accumulated_sum):
    if current_number == 11:
        return accumulated_sum
    return sum_recursive(current_number + 1, accumulated_sum + current_number)


def countdown(n):
    print(n)
    if n == 0:
        return
    countdown(n - 1)   # Recursive call
