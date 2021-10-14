n, m = map(int, input().split())

def f(a, b):
    if (a == 1 or b == 1):
        return 1
    else:
        return f(a-1, b) + f(a, b-1)

print(f(n, m))