n = 5
m = 5

world = [
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 3, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

# for i in range(n):
#     world.append([])
#     for j in range(m):
#         world[i].append()

def findRobot(list):
    for i in range(n):
        for j in range(m):
            if list[i][j] == 3:
                return [i, j]
            
robot = findRobot(world)

def escape(robot):
    robot = findRobot(world)
    location = [robot]
    checkPoint = []
    cnt = 0
    while True:
        checkPoint.clear()
        for i in range(len(location)):
            if location[i][0]+1 < n and location[i][1]+1 < m:
                if world[location[i][0]+1][location[i][1]] == 0:
                    checkPoint.append([location[i][0]+1, location[i][1]])
                if world[location[i][0]-1][location[i][1]] == 0:
                    checkPoint.append([location[i][0]-1, location[i][1]])
                if world[location[i][0]][location[i][1]+1] == 0:
                    checkPoint.append([location[i][0], location[i][1]+1])
                if world[location[i][0]][location[i][1]-1] == 0:
                    checkPoint.append([location[i][0], location[i][1]-1])
                world[location[i][0]][location[i][1]] = 1
            else:
                return cnt+1
        location.clear()
        for i in range(len(checkPoint)):
            location.append(checkPoint[i])
        cnt += 1

print(escape(robot))