# data = input().split()
# p = int(data[0])
# day = int(data[1])

p = 1
day = 4

def v(p, day):
    if day == 0:
        return p
    elif day == 1:
        return p
    elif day == 2:
        return p + (v(p, day-2) * 2)
    else:
        return p + (v(p, day-2) * 2) + v(p, day-3)
    
print(v(p, day))