# a0
data = [
    ["income", "1", "1", "1000"],
    ["outcome", "3", "15", "500"],
    ["income", "2", "1", "1000"],
    ["income", "6", "3", "1000"],
    ["outcome", "11", "20", "3000"],
    ["outcome", "12", "6", "2500"],
    ["income", "4", "1", "2000"],
    ["outcome", "1", "2", "150"],
    ["income", "12", "5", "6500"],
    ["outcome", "10", "9", "310"],
]

# a1
# n = int(input())
# data = [input().split for _ in range(n)]

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
