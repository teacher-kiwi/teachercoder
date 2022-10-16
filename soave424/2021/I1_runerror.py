# 급식 순서
# run error

import itertools
import numpy as np


n=input()
l = [list(map(int, input().split())) for _ in range(int(n))]
list=list(itertools.permutations(range(int(n))))


matrix1=np.array(l)
matrix2=np.array(list)



largest=0
for r in range(len(matrix2)):
    c=0
    for i in range(int(n)-1):
        a=matrix2[r][i]
        b=matrix2[r][i+1]
        c+=matrix1[a][b]
        if c>largest:
            largest=c
print(largest)

        
