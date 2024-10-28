def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


print(gcd(1680, 640))
print(gcd(7, 3))
