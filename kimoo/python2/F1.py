n = int(input())
pi = list(map(float, input().split()))
t = float(input())

d = []
for i in range(n):
    d.append(abs(pi[i] - t))

print("{:.2f}".format(pi[d.index(min(d))]))