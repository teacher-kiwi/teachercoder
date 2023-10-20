# b0
a, b, c, d = 0, 1, 4, 9

# b1
# a, b, c, d = map(int, input().split())

def solve(a: int, b: int, c: int, d: int, count: int):
    if (a, b, c, d) == (0, 0, 0, 0):
        print(count)
    else:
        a, b, c, d = abs(a - b), abs(b - c), abs(c - d), abs(d - a)
        solve(a, b, c, d, count + 1)

solve(a, b, c, d, 0)