data1 = input().split()

world = []
for i in range(int(data1[0]) +2):
    world.append([])
    for j in range(int(data1[1]) +2):
        world[i].append(-1)

for i in range(int(data1[0])):
    data2 = input()
    for j in range(int(data1[1])):
        world[i+1][j+1] = int(data2[j])

for i in range(len(world)):
    for j in range(len(world[0])):
        if world[i][j] == 3:
            world[i][j] = 2
            break

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
robot = 1
while True:
    cnt = 0
    robot += 1
    for i in range(len(world)-2):
        for j in range(len(world[0])-2):
            if world[i+1][j+1] == robot:
                for k in range(4):
                    if world[i+1+dx[k]][j+1+dy[k]] == 0:
                        world[i+1+dx[k]][j+1+dy[k]] = robot+1
                        cnt += 1
    if cnt == 0: break

checklist = []
for i in range(len(world)-2):
    if i == 0 or i == len(world)-3:
        for j in range(len(world[0])-2):
            if world[i+1][j+1] != 0 and world[i+1][j+1] != 1:
                if world[i+1][j+1] not in checklist:
                    checklist.append(world[i+1][j+1])
    else:
        if world[i+1][1] != 0 and world[i+1][1] != 1:
            if world[i+1][1] not in checklist:
                checklist.append(world[i+1][1])
        if world[i+1][-2] != 0 and world[i+1][-2] != 1:
            if world[i+1][-2] not in checklist:
                checklist.append(world[i+1][-2])

if len(checklist) != 0:
    print(min(checklist) - 1)