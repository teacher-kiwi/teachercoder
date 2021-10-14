R, C, TR, TC = map(int, input().split())

n = int(input())

block = []
for i in range(n):
    BR, BC = map(int, input().split())
    block.append([BR, BC])

world = [[0 for i in range(C)] for j in range(R)]
world[0][0] = 1
for i in range(len(block)):
    world[block[i][0]-1][block[i][1]-1] = -1

x = [1, -1, 0, 0]
y = [0, 0, 1, -1]

chk = 1
cnt = 1
while(chk != 0):
    chk = 0
    for i in range(R):
        for j in range(C):
            if (world[i][j] == cnt):
                for k in range(4):
                    if (i+x[k]<0 or i+x[k]>R-1 or j+y[k]<0 or j+y[k]>C-1):
                        continue
                    elif (world[i+x[k]][j+y[k]] == 0):
                        world[i+x[k]][j+y[k]] = cnt + 1
                        chk += 1
    cnt += 1

if (world[TR-1][TC-1] == 0):
    print(-1)
else:
    print(world[TR-1][TC-1] - 1)