r = int(input()) // 2

res = 0
for n in range(1, r+1):
    h = r
    while r**2 - n**2 < h**2:
        h -= 1
    res += h


    h = r
    h2 = 0
    while r**2 - n**2 < h**2:
        h -= 1
    
    while h2 < n / 3**0.5 and h2 < h:
        h2 += 1
    res += (h - h2)

print(res * 2)