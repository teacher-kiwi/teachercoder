n=3
m=7
mat=[[0,5,7,6,4,1,7],[3,1,4,3,5,10,2],[7,3,7,4,8,2,4]]

target_n=3
target_m=7


dx=[-1,1,0,0]
dy=[0,0,-1,1]
visited = [[0 for _ in range(m)] for _ in range(n)]

x=target_n-1
y=target_m-1
max=mat[target_n-1][target_m-1]

def visit_mat(x,y):
  li=[]
  global max
  min=1000000
  visited[x][y]=1
  if mat[x][y]>=max:
    max=mat[x][y]
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if 0<=nx<n and 0<=ny<m:
      if visited[nx][ny]==0:
        if mat[nx][ny]<=min:
          li=[]
          min=mat[nx][ny]
          li.append([nx,ny])
          print(li)
          print(min)
          # visit_mat(li[0][0],li[0][1])  
          

          
visit_mat(x,y)          
visit_mat(1,6)
visit_mat(0,6)
visit_mat(0,5)
visit_mat(0,4)
visit_mat(1,4)
visit_mat(1,3)
visit_mat(1,2)
visit_mat(1,1)
visit_mat(1,0)

print(visited)
print(max)
