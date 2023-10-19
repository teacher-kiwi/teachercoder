a, b, k = map(int, input().split())

n0 = a//b
m = a % b

list_N = []

for i in range(k+1):
    n = 10*m // b
    m = 10*m % b
    list_N.append(n)

if (list_N[-1] >= 5):
    list_N[-2] += 1
    for i in range(k, 0, -1):
        if list_N[i] >= 10:
            list_N[i] -= 10
            list_N[i-1] += 1
    if list_N[0] == 10:
        n0 += 1
        list_N[0] = 0
list_N.pop()
original_number = str(n0)+"." + "".join(map(str, list_N))

print(original_number)


# 입력 3 7 8
# 출력 0.42857143
