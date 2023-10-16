# e0
# n = 5

# e1
n = int(input())

dp = {2: [[2, 1]], 3: [[3, 1]]}


def solve(n: int):
    if n <= 3:
        return dp[n]
    if not dp.get(n):
        temp = []
        for i in range(2, n-1):
            _sum = 0
            for num, count in solve(n-i):
                _sum += ((i + num - 1) * count) % 10000000
            temp.append([i, _sum])
        temp.append([n, 1])
        dp[n] = temp
    return dp[n]

res = 0
for _, count in solve(n):
    res += count
    res %= 10000000

print(res)
