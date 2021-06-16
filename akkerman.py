def calculate_akkerman_function(m, n):
    if m == 0:
        return n+1
    if n == 0:
        return calculate_akkerman_function(m-1, 1)
    if n > 0:
        return calculate_akkerman_function(m-1, calculate_akkerman_function(m, n-1))


print(calculate_akkerman_function(1, 0))
