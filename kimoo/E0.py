# data1 = input().split()
# world = [int(data1[0]), int(data1[1])]
# target = [int(data1[2]), int(data1[3])]
# n = int(input())
# bList = []
# for i in range(n):
#     data2 = input().split()
#     bList.append([int(data2[0]), int(data2[1])])
world = [3, 3]
target = [3, 2]
bList = [[3, 1], [2, 2]]

i = [[1, 1]]
checkPoint = []
cnt = 0

while target not in checkPoint:
    checkPoint.clear()
    for j in range(len(i)):
        if [i[j][0]+1, i[j][1]] not in bList and i[j][0]+1 <= world[0]:
            checkPoint.append([i[j][0]+1, i[j][1]])
        if [i[j][0]-1, i[j][1]] not in bList and i[j][0]-1 > 0:
            checkPoint.append([i[j][0]-1, i[j][1]])
        if [i[j][0], i[j][1]+1] not in bList and i[j][1]+1 <= world[1]:
            checkPoint.append([i[j][0], i[j][1]+1])
        if [i[j][0], i[j][1]-1] not in bList and i[j][1]-1 > 0:
            checkPoint.append([i[j][0], i[j][1]-1])
    i.clear()
    for j in range(len(checkPoint)):
        i.append(checkPoint[j])
    cnt += 1

print(cnt)