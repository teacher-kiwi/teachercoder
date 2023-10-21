word = input()

res = [0]

target = "GTPC"

def dfs(i, j):
    if i == 4:
        res[0] += 1
        return
    pos = []
    for k in range(j, len(word)):
        if word[k] == target[i]:
            pos.append(k)
    for n in pos:
        dfs(i+1, n)

dfs(0, 0)
print(res[0])