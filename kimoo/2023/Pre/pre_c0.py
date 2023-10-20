# c0
board = [
    ["#", "#", "A", "B"],
    ["B", "A", "#", "#"],
    ["A", "#", "#", "D"],
    ["C", "D", "B", "A"],
]
# board = [
#     ["A", "B", "#", "#"],
#     ["C", "D", "B", "A"],
#     ["D", "C", "A", "B"],
#     ["B", "A", "#", "#"],
# ]
# board = [
#     ["A", "B", "B", "D"],
#     ["C", "D", "C", "#"],
#     ["D", "C", "A", "B"],
#     ["B", "A", "D", "C"],
# ]

# c1
# board = [input().split() for _ in range(4)]


ROW, COL = len(board), len(board[0])
res = [0]

def check():
    chars = set()
    for r in range(4):
        chars.clear()
        for i in range(4):
            char = board[r][i]
            if char in chars:
                return False
            if char != "#":
                chars.add(char)

    for c in range(4):
        chars.clear()
        for i in range(4):
            char = board[i][c]
            if char in chars:
                return False
            if char != "#":
                chars.add(char)

    for r, c in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        chars.clear()
        for i, j in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            char = board[r + i][c + j]
            if char in chars:
                return False
            if char != "#":
                chars.add(char)
    
    return True

blank = []
for r in range(ROW):
    for c in range(COL):
        if board[r][c] == "#":
            blank.append((r, c))

def dfs(blank: list, d):
    if not blank:
        # print(board)
        res[0] += 1
        return
    
    r, c = blank.pop()
    
    chars = {"A", "B", "C", "D"}
    for i in range(4):
        chars.discard(board[r][i])
        chars.discard(board[i][c])
    for i, j in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        chars.discard(board[(r//2)*2 + i][(c//2)*2 + j])

    for char in chars:
        board[r][c] = char
        dfs(blank, d+1)
        board[r][c] = "#"

    blank.append((r, c))

if check():
    dfs(blank, 0)
print(res[0])