n = int(input(), 2)
res = [float("inf")]
stack = [(0, n)]


def dfs(i, n):
    if n == 0:
        res[0] = min(i, res[0])
        return

    mask = 1 << (len(bin(n)) - 3)
    dfs(i+1, n ^ mask)

    mask = 0
    for j in range(len(bin(n)) - 2):
        mask |= (1 << j)
    dfs(i+1, n ^ mask)


b = 1
while b < n:
    b *= 2
dfs(0, b-1-n)
print(res[0])
