n, k = map(int, input().split())

def x(n, k):
    if (k <= 1):
        return n
    elif (k == 2):
        return n + x(n*2, k-2)
    else:
        return n + x(n*2, k-2) + x(n, k-3)

print(x(n, k))