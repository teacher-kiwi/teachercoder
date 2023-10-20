import itertools

n = int(input())
like = [list(map(int, input().split())) for _ in range(n)]

a = [i+1 for i in range(n-1)]
order = list(itertools.permutations(a))

sum = 0
for i in range(len(order)):
    test = 0
    for j in range(n-1):
        if j == 0:
            test += like[0][order[i][0]]
        else:
            test += like[order[i][j-1]][order[i][j]]
    if sum < test:
        sum = test

print(sum)