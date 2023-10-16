# e0
n = 5

# e1
# n = int(input())

combinations = []


def solve(n: int):

    def dfs(n, li):
        if n <= 3:
            return
        for i in range(2, n-1):
            combinations.append(li + [i, n-i])
            dfs(n-i, li + [i])

    dfs(n, [])
    res = 0
    for combination in combinations:
        temp = 1
        for i in range(len(combination)-1):
            temp *= combination[i] + combination[i+1] - 1
            temp %= 10000000

        res += temp
        res %= 10000000
    print(res + 1)

solve(n)