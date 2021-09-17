from math import gcd

n = 198

def lcm(x, y):
    return x * y // gcd(x, y)

def mlcm(n):
    if n == 1:
        return 1
    elif lcm(n, n-1) == n * (n-1):
        return n * (n-1)
    else:
        n -= 1
        return mlcm(n)

print(mlcm(n))