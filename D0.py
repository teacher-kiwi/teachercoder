k = 10
n = 11
num = 0

def digitSum(num):
    digitSum = 0
    while num // 10 > 0:
        digitSum += num % 10
        num = num // 10
    return digitSum + num

while n > 0:
    num += 1
    while digitSum(num) != k:
        num += 1
    n -= 1
    
print(num)