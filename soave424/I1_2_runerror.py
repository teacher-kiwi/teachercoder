# 급식 순서
# run error

import itertools


'''
matrix1 =[[0,1,10,20],[1,0,12,4],[10,12,0,7],[20,4,7,0]]

'''


n=input()
matrix1= [list(map(int, input().split())) for _ in range(int(n))]
matrix2 =list(itertools.permutations(range(int(n))))

largest=0
for r in range(len(matrix2)):
    if int(matrix2[r][0])==0:
        c=0
        for i in range(int(n)-1):
            a=matrix2[r][i]
            b=matrix2[r][i+1]
            c+=matrix1[a][b]
            if c>largest:
                largest=c

print(largest)

