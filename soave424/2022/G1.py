# n,m=map(int,input().split())
# n,m=3,7
n,m=5,5
# n,m=3,3

# mat=[list(map(int,input().split())) for _ in range(n)]
# mat=[[0,5,7,6,4,1,7],[3,1,4,3,5,10,2],[7,3,7,4,8,2,4]]
mat=[[0,5,7,6,4],[3,1,4,3,5],[7,3,7,4,5],[1,2,8,3,2],[7,8,6,2,5]]
# mat=[[0,100,200],[1000,100,2],[100,150,22]]

# target_n,target_m=map(int,input().split())
target_n=4
target_m=1

tx=target_n-1
ty=target_m-1
x=0
y=0

dx=[-1,1,0,0]
dy=[0,0,-1,1]

visited = [[0 for _ in range(m)] for _ in range(n)]

visited[0][0]=1

ran = []
for i in range(4): # 상하좌우 탐색
  nx=x+dx[i]
  ny=y+dy[i]
  if 0<=nx<n and 0<=ny<m: #그리드 범위 내 
    if visited[nx][ny]==0: #방문하지 않은 곳 중에서
      ran.append(mat[nx][ny])
min=min(ran)


def find(x,y):
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if 0<=nx<n and 0<=ny<m: #그리드 범위 내 
      if visited[nx][ny]==0:
        visited[nx][ny]=1
        if mat[nx][ny]<=min:
          find(nx,ny)
        else:
          return    

min += 1

find(3,1)
if visited[tx][ty]==1:
  print("done",min-1)
print(visited)
