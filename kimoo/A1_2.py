# A1_2 

import math

data = list(input().split())

teacher = int(data[0])
count = int(data[1])

def buyBread(teacher):
    bread = teacher * count
    if bread <= 30:
        return 9000
    elif bread <= 50:
        return 15000
    elif bread <= 60:
        return 18000
    elif bread <= 80:
        return 24000
    elif bread <= 90:
        return 27000
    elif bread <= 100:
        return 30000
    elif bread % 30 > 0 and bread % 30 <= 10:
        return math.ceil((bread - 100) / 30) * 9000 + 30000
    elif bread % 30 > 10 and bread % 30 <= 20:
        return math.ceil((bread - 50) / 30) * 9000 + 15000
    else:
        return math.ceil(bread / 30) * 9000
    
costBread = buyBread(teacher)

print(costBread)
