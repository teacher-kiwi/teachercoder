n,m = map(int,input().split())
mat = []
for i in range(1,n+1):
  for j in range(1,m+1):
    mat.append([i,j])
  
# 직사각형 그리드의 모든 경로를 가져오는 재귀 함수
# 셀(i, j)에서 시작하여 마지막 셀(M-1, N-1)에서 끝나는 
C = 0
def paths(mat, route=[], i=0, j=0):
    global C
    # 베이스 케이스
    if not mat or not len(mat):
        return
    # `M × N` 매트릭스
    (M, N) = (len(mat), len(mat[0]))
    #는 경로에 현재 셀을 포함합니다.
    route.append(mat[i][j])
    # 마지막 셀에 도달한 경우
    if i == M - 1 and j == N - 1:
        # print(route)
        C+=1
    else:
        # 아래로 이동
        if i + 1 < M:
            paths(mat, route, i + 1, j)
        # 오른쪽으로 이동해라
        if j + 1 < N:
            paths(mat, route, i, j + 1)
 
    # 역추적: 경로에서 현재 셀 제거
    route.pop()
 
paths(mat)
print(C)