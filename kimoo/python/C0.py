x = 3
y = 3

xList = []
for i in range(x):
    xList.append(1)

for i in range(y-1):
    for i in range(x-1):
        xList[i+1] += xList[i]

print(xList[x-1])