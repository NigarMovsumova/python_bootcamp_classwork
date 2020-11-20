def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

n = int(input('Enter number:'))
baba = list(primes(n))
baba = list(dict.fromkeys(baba))
print(baba)