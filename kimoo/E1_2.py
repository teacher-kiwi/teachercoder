data1 = input().split()
worldSize = [int(data1[0]), int(data1[1])] #월드의 크기(행개수 r, 열개수 c)

world = []
for i in range(worldSize[0] +2):
    world.append([])
    for j in range(worldSize[1]+2):
        if i == 0 or i == worldSize[0] +1:
            world[i].append(-2)
        elif j == 0 or j == worldSize[1] +1:
            world[i].append(-2) # 움직일 수 없는 곳은 -2
        else:
            world[i].append(-1) # 움직일 수 있는 곳은 -1

target = [int(data1[2]), int(data1[3])] #목적지 좌표(tr, tc)
# world[target[0]][target[1]] = -3 # 목적지는 -3

n = int(input()) #장애물의 개수
for i in range(n):
    data2 = input().split()
    world[int(data2[0])][int(data2[1])] = -2 #장애물 리스트 저장(br, bc)

world[1][1] = 0

def findRoute(target, world):
    cnt = 0
    if target == [1, 1]:
        return cnt
    else:
        while True:
            change = 0
            for i in range(len(world)):
                for j in range(len(world[i])):
                    if world[i][j] == cnt:
                        if world[i+1][j] == -1:
                            world[i+1][j] = cnt +1
                            change += 1
                        if world[i-1][j] == -1:
                            world[i-1][j] = cnt +1
                            change += 1
                        if world[i][j+1] == -1:
                            world[i][j+1] = cnt +1
                            change += 1
                        if world[i][j-1] == -1:
                            world[i][j-1] = cnt +1
                            change += 1
            if change == 0: 
                return world[target[0]][target[1]]
            else: 
                cnt += 1


print(findRoute(target, world))