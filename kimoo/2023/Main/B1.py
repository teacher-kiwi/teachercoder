h, c = map(int, input().split())

res = 0

if c * 2 <= h:
    print(c)
else:
    print(h // 2)