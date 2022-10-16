# 급식 순서
# correct

import itertools


matrix1=[[0,1,10,4],
   [1,0,12,20],
   [10,12,0,7],
   [4,20,7,0]]


list=list(itertools.permutations('0123',4))
largest=0
for i in range(len(list)):
    if int(list[i][0])==0:
        newa=0
        for n in range(3):
            a=matrix1[int(list[i][n])][int(list[i][n+1])]
            newa=newa+a
            if newa >= largest:
                largest=newa


print(largest)

