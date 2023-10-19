# c0
# a, b, k = 999999999, 100000000, 6

# c1
a, b, k = map(int, input().split())

res = []

def solve(a: int, b: int, k: int):
    while k:
        res.append(a // b)
        a = (a % b) * 10
        k -= 1
    
    if res[-1] >= 5:
        res[-1] = 10
        for i in range(len(res)-1, 0, -1):
            if res[i] == 10:
                res[i] = 0
                res[i-1] += 1
            else:
                break
    res.pop()
    print(f"{res[0]}.{''.join(map(str,res[1:]))}")

solve(a, b, k+2)