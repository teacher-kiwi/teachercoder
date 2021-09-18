data = input().split()

k = int(data[0])
n = int(data[1])
num = [0, 0, 0, 0, 0, 0]
result = 0

if k > 9:
    num[0] = 9
    if k - 9 > 9:
        num[1] = 9
        num[2] = k - 18
    else:
        num[1] = k -9
else:
    num[0] = k
    
def next(num, i):
    if num[i] != 0 and num[i+1] != 9:
        num[i] -= 1
        num[i+1] += 1
    elif num[i] == 0 or num[i+1] == 9:
        next(num, i+1)
        sum = 0
        for j in range(i+2):
            sum += num[j]
        for j in range(i+2):
            if sum > 9:
                num[j] = 9
                sum -= 9
            else:
                num[j] = sum
                sum = 0

for i in range(n-1):
    next(num, 0)

for i in range(6):
    result += num[i] * (10 ** i)

print(result)