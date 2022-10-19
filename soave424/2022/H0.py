m,n = 5, 5
map = [[30,26,26,21,13],[5,26,22,16,9],[4,17,23,24,7],[26,16,9,12,4],[19,28,27,16,10]]
# m,n=5,2
# map=[[8,9,10,3,2],[7,6,5,4,1]]


dx=[-1,1,0,0]
dy=[0,0,-1,1]
cnt=0

def dp_waterslide(y,x):
  if dp[y][x]!=-1 : 
    return dp[y][x]
  if y==m-1 and x==n-1 : 
    return 1
  dp[y][x]=0
  li.append(map[y][x])

  for i in range(0,4):
    ny = y+dy[i]
    nx = x+dx[i]
    if 0<=ny<m and 0<=nx<n and map[y][x]>map[ny][nx]:
      dp[y][x] += dp_waterslide(ny,nx)
  return dp[y][x]

for i in range(m):
  for j in range(n):
    dp = [[-1]*n for _ in range(m)]
    li=[]
    dp_waterslide(i,j)
    print(i,j, li)
