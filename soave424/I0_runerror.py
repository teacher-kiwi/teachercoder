# 급식 순서
# run error


import itertools
import numpy as np
list=list(itertools.permutations('0123',4))
l=[[0,1,10,4],
   [1,0,12,20],
   [10,12,0,7],
   [4,20,7,0]]
matrix1=np.array(l)
matrix2=np.array(list)
largest=0
for n in range(len(matrix2)):
    a=matrix1[int(matrix2[n][0])][int(matrix2[n][1])]
    b=matrix1[int(matrix2[n][1])][int(matrix2[n][2])]
    c=matrix1[int(matrix2[n][2])][int(matrix2[n][3])]
    if a+b+c >= largest:
        largest=a+b+c
print(largest)
