n, m = map(int, input().split())
target = input()
board = [input() for _ in range(n)]

pos = []

d = {
    0: (-1, 0),
    1: (-1, 1),
    2: (0, 1),
    3: (1, 1),
    4: (1, 0),
    5: (1, -1),
    6: (0, -1),
    7: (-1, -1),
}

for r in range(n):
    for c in range(m):
        if target[0] == board[r][c]:
            if r > 0 and target[1] == board[r-1][c]:
                pos.append((r, c, 0))
            if r > 0 and c < m-1 and target[1] == board[r-1][c+1]:
                pos.append((r, c, 1))
            if c < m-1 and target[1] == board[r][c+1]:
                pos.append((r, c, 2))
            if r < n-1 and c < m-1 and target[1] == board[r+1][c+1]:
                pos.append((r, c, 3))
            if r < n-1 and target[1] == board[r+1][c]:
                pos.append((r, c, 4))
            if r < n-1 and c > 0 and target[1] == board[r+1][c-1]:
                pos.append((r, c, 5))
            if c > 0 and target[1] == board[r][c-1]:
                pos.append((r, c, 6))
            if r > 0 and c > 0 and target[1] == board[r-1][c-1]:
                pos.append((r, c, 7))
            
res = []
def dfs(i, r, c, n):
    if i == len(target):
        res.append(f"{r} {c} {n}")
        return
    try:
        if board[r+(d[n][0]*i)][c+(d[n][1]*i)] == target[i]:
            dfs(i+1, r, c, n)
    except:
        return


for r, c, n in pos:
    dfs(1, r, c, n)

print(res[0])