k, n = map(int, input().split())

def sum(num):
    sum = 0
    for i in range(len(str(num))):
        sum += int(num / (10 ** i))  % 10
    return sum

num = 0
cnt = 0
li = [0 for i in range(10000000)]

while (li[n-1] == 0):
    num += 1
    if (sum(num) == k):
        li[cnt] = num
        cnt += 1


print(li[n-1])
