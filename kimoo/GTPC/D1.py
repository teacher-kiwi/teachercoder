r, c = map(int, input().split())

li = []

for i in range(r):
    li.append(list(map(int, input().split())))

for i in range(1, r+c+1):
    j = r+c-i
    