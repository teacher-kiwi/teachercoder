# 급식 순서
# timelimit
#import time
from itertools import permutations
import itertools

#matrix1 =[[0,1,10,20],[1,0,12,4],[10,12,0,7],[20,4,7,0]]

n=input()
matrix1= [list(map(int, input().split())) for _ in range(int(n))]
#start_time = time.time() # 측정 시작
matrix2 =[]
for i in permutations(range(int(n))):
    if i[0]==0:
        matrix2.append(i)
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

# 프로그램 소스코드
#end_time = time.time() # 측정 종료
#print("time:", end_time - start_time) # 수행 시간 출력

