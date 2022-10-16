
n,m=map(int,input().split())
mat=[list(map(int,input().split())) for _ in range(n)]

graph=[[] for _ in range((n*m)+1)]

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
      if num<mat[nx][ny]:
        graph[num].append(mat[nx][ny])

visited=[False]*len(graph)
length=[]
def dfs (graph,v,visited):
  global length
  visited[v]=True
  length.append(v)
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)

dfs(graph,1,visited)
print(len(length))