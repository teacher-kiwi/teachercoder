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
  # print(li[0][0])
  if li[0][0]==0 and li[0][1]==0:
    return
  elif mat[li[0][0]][li[0][1]]>max:
    visit_mat(target_n-1,target_m-1)
  else:
    visit_mat(li[0][0],li[0][1])
  # print(li[0])
  # print(min)
  
          

          
visit_mat(x,y)          
# visit_mat(1,6)
# visit_mat(0,6)
# visit_mat(0,5)
# visit_mat(0,4)
# visit_mat(1,4)
# visit_mat(1,3)
# visit_mat(1,2)
# visit_mat(1,1)
# visit_mat(1,0)

# print(visited)
print(max)
