def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

print(fact(7))


def fact2(n):
    if n <= 1:
         return 1
    return n * fact2(n - 1)

print(fact2(5))


def sum(n):
    if n <= 1:
        return 1
    return n + sum(n-1)

print(sum(5))