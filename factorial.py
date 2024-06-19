def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


assert factorial(5) == 120
assert factorial(6) == 720
