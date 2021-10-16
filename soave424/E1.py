from itertools import permutations
import sys

n=int(input())
lis=list(map(int,input().split()))

mainlis=[i for i in permutations(range(1,n+1))]


for k in range(n):
  mainlis=[i for i in mainlis if i[k]!=lis[k]]
print(len(mainlis))

print(mainlis)
