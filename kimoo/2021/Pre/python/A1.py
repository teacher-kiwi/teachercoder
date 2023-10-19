data = list(input().split())

teacher = int(data[0])
count = int(data[1])

def calcBread(bread, start):
    if bread <= start:
        return start
    else:
        start += 30
        return calcBread(bread, start)

def buyBread(teacher):
    bread = teacher * count
    case1 = calcBread(bread, 30)
    case2 = calcBread(bread, 50)
    case3 = calcBread(bread, 100)
    return min(case1, case2, case3)

costBread = buyBread(teacher) * 300

print(costBread)