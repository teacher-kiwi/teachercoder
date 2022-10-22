

# n,m=map(int,input().split())
#n,m=3,7
#n,m=5,5
n,m=3,3

# mat=[list(map(int,input().split())) for _ in range(n)]
# mat=[[0,5,7,6,4,1,7],[3,1,4,3,5,10,2],[7,3,7,4,8,2,4]]
# mat=[[],[],[],[],[]]
mat=[[0,100,200],[1000,100,2],[100,150,22]]

# target_n,target_m=map(int,input().split())
target_n=2
target_m=3


dx=[-1,1,0,0]
dy=[0,0,-1,1]

x=target_n-1
y=target_m-1
max=mat[target_n-1][target_m-1]
visited = [[0 for _ in range(m)] for _ in range(n)]
visited[x][y]=1

down=[22,100,200]

#타겟에서부터 거꾸로 가면서 가능한 거리 내 가장 최소 선택 
def visit_mat(x,y):
  li=[]
  global max, target_m, target_n
  min=1000000 # 최대 가능한 수 
  visited[x][y]=1 # 방문처리 
  if mat[x][y]>=max: # 최대 입장료 변경
    max=mat[x][y]
  for i in range(4): # 상하좌우 탐색
    nx=x+dx[i]
    ny=y+dy[i]
    if 0<=nx<n and 0<=ny<m: #그리드 범위 내 
      if visited[nx][ny]==0: #방문하지 않은 곳 중에서 
        if mat[nx][ny]<min: #가장 최소인 거리 선택 
          li=[] #리스트 초기화 (큰 값이 먼저 입력된 경우 지우기 위해서 )
          min=mat[nx][ny] #최소 선택
          li.append([nx,ny]) #리스트에 넣기 

  if len(li)>0:
    if li[0][0]!=0 or li[0][1]!=0:
      visit_mat(li[0][0],li[0][1])
  return max
  # print(li[0])



for i in range(4): # 맨 처음 후보 3개 
  d_nx=x+dx[i]
  d_ny=y+dy[i]
  if 0<=d_nx<n and 0<=d_ny<m: #그리드 범위 내 
    visited([[0]*m])
    print(d_nx,d_ny)

    print(visit_mat(d_nx,d_ny))









