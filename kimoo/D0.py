k = 10
n = 10000
num = 0

def digitSum(num):
    if num < 10:
        return num
    return digitSum(num // 10) + num % 10

while n > 0:
    num += 1
    if digitSum(num) == k:
        n -= 1
    
print(num)