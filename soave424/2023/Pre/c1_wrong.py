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
    list_N.pop()

list_N.reverse()

for i in range(k-1):
    if list_N[i] >= 10:
        list_N[i+1] += 1
        list_N[i] -= 10

if list_N[-1] == 10:
    n0 += 1
    list_N[-1] -= 10


list_N.reverse()

original_number = str(n0)+"." + "".join(map(str, list_N))

print(original_number)
