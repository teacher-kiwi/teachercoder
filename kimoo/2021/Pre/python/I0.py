n = int(input())

like = []
for i in range(n):
    like.append([])
    data2 = input().split()
    for j in range(n):
        like[i].append(int(data2[j]))

# like = [
#     [0, 1, 1, 1, 100],
#     [1, 0, 2, 3, 1],
#     [1, 2, 0, 10, 5],
#     [1, 3, 10, 0, 7],
#     [100, 1, 5, 7, 0]
# ]

point = 0

def findBest(point, index, list):
    numMax = max(list[index])
    if numMax == -1:
        return point
    else:
        point += numMax
        indexMax = like[index].index(numMax)
        list[index][indexMax] = -1
        for i in range(len(like)):
            list[i][index] = -1
        return findBest(point, indexMax, list)

print(findBest(point, 0, like))