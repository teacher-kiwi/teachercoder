
# n,m=map(int,input().split())
# mat=[list(map(int,input().split())) for _ in range(n)]

n,m=5,5
mat=[[30,26,26,21,13],[5,26,22,16,9],[4,17,23,24,7],[26,16,9,12,4],[19,28,27,6,10]]
graph=[[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],]

def make_graph(mat,graph) :
  for x in range(len(mat)):
    for y in range(len(mat[0])):
      num=mat[x][y]
      dx=[0,0,1,-1]
      dy=[1,-1,0,0]
      for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>n-1 or ny>m-1:
          continue
        if num>mat[nx][ny]:
          graph[x][y].append([nx,ny])

def dfs (graph,x,y,z,visited):
  visited[x][y]=True
  if not len(graph[x][y])<0:
    dfs(graph,x,y,z,visited)
    


  # global n,m,
  # visited[x][y]=True
  # for i in range(n):
  #   for j in range(m):
  #     if not visited[i][j]:
  #       dfs(graph,i,j,visited)
        
make_graph(mat,graph)
# dfs(graph,0,0,visited)

for i in range(n):
  for j in range(m):
    # for ii in range(len(graph[i][j])):
    visited=[[False]*m for _ in range(n)]
    dfs(graph,i,j,visited)
      
    
    
    
    #   arr = []
    #   arr.append([i,j])
    #   visited[i][j]=True
    #   if not len(graph[i][j])<0:
      
    #     next=graph[i][j][0]
    #     arr.append(next)
    #     visited[next[0]][next[1]]=True

        
    #     if not len(graph[next[0]][next[1]])<2:
    #       next2=graph[next[0]][next[1]][1]
    #       arr.append(next2)
    #       visited[next2[0]][next2[1]]=True
    # print(arr)
        # if not len(graph[next[0]][next[0]])<0:
        #   next2=graph[]
          
        
      
# print(arr)
    


# print(graph)

def waterslide (x,y) :
  global n,m
  visited=[[False]*m for _ in range(n)]
  visited[x][y] = True
