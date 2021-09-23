 # 급식 순서
import time
from itertools import permutations
import sys


n=input()
matrix1= [list(map(int, sys.stdin.readline().split())) for _ in range(int(n))]
start_time = time.time()



matrix2=[i for i in permutations(range(int(n))) if i[0]==0]
largest=0
for r in range(len(matrix2)):
    c=0
    for i in range(int(n)-1):
        c+=matrix1[matrix2[r][i]][matrix2[r][i+1]]
    if c>largest:
        largest=c
print(largest)


end_time = time.time() 
print("time:", end_time - start_time) 



