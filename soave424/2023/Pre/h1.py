
list = list(map(int, input().split()))

# list = [1, 0, 0, 1, 1, 1, 0, 1, 1, 0]


def flip(n):
    if n == 0:
        n = 1
    else:
        n = 0
    return n


def change(m):
    list[m] = flip(list[m])
    list[m+1] = flip(list[m+1])
    list[m+2] = flip(list[m+2])


k = 0
while True:
    if all(element == 0 for element in list):
        break
    for i in range(10):
        if list[i] == 1:
            change(i)
            k += 1
print(k)
