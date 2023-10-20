n = int(input())
data = [input().split() for _ in range(n)]

res = [[i, 0, 0, 0] for i in range(1, 13)]
for type, m, _, t in data:
    m, t = int(m), int(t)
    if type == "income":
        res[m-1][1] += t
        res[m-1][3] += t
    else:
        res[m-1][2] += t
        res[m-1][3] -= t

for data in res:
    print(" ".join(map(str, data)))
