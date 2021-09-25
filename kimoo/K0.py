import itertools

# mapSize = list(map(int, input().split()))

# map = [list(map(int, input())) for _ in range(mapSize[0])]

map = [
    [1, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1]
]

points = []
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == 1:
            points.append([i, j])

threePoint = list(itertools.combinations(points, 3))
area = 0

for i in range(len(threePoint)):
    triangle = threePoint[i]
    if triangle[0][0] == triangle[1][0] and triangle[1][0] == triangle[2][0]:
        continue
    if triangle[0][1] == triangle[1][1] and triangle[1][1] == triangle[2][1]:
        continue
    if triangle[0][0] == triangle[1][0]:
        if area < abs((triangle[0][1] - triangle[1][1]) * (triangle[0][0] - triangle[2][0]) / 2):
            area = abs((triangle[0][1] - triangle[1][1]) * (triangle[0][0] - triangle[2][0]) / 2)
    elif triangle[0][0] == triangle[2][0]:
        if area < abs((triangle[0][1] - triangle[2][1]) * (triangle[0][0] - triangle[1][0]) / 2):
            area = abs((triangle[0][1] - triangle[2][1]) * (triangle[0][0] - triangle[1][0]) / 2)
    elif triangle[1][0] == triangle[2][0]:
        if area < abs((triangle[1][1] - triangle[2][1]) * (triangle[0][0] - triangle[2][0]) / 2):
            area = abs((triangle[1][1] - triangle[2][1]) * (triangle[0][0] - triangle[2][0]) / 2)
    if triangle[0][1] == triangle[1][1]:
        if area < abs((triangle[0][0] - triangle[1][0]) * (triangle[0][1] - triangle[2][1]) / 2):
            area = abs((triangle[0][0] - triangle[1][0]) * (triangle[0][1] - triangle[2][1]) / 2)
    elif triangle[0][1] == triangle[2][1]:
        if area < abs((triangle[0][0] - triangle[2][0]) * (triangle[0][1] - triangle[1][1]) / 2):
            area = abs((triangle[0][0] - triangle[2][0]) * (triangle[0][1] - triangle[1][1]) / 2)
    elif triangle[1][1] == triangle[2][1]:
        if area < abs((triangle[1][0] - triangle[2][0]) * (triangle[0][1] - triangle[2][1]) / 2):
            area = abs((triangle[1][0] - triangle[2][0]) * (triangle[0][1] - triangle[2][1]) / 2)

print(area)