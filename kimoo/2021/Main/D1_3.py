r, c = map(int, input().split())
v = [list(map(int, input().split())) for _ in range(r)]

# r, c = 3, 3
# v = [
#   [-10, -10, -10], 
#   [-10, -10, -10], 
#   [-10, -10, -10]
# ]


s = []
for r1 in range(r):
  s.append([])
  for c1 in range(c):
    s[r1].append(0)
    if r1==0 and c1==0:
      s[r1][c1] = v[r1][c1]
    elif r1==0:
      s[r1][c1] = v[r1][c1] + s[r1][c1-1]
    elif c1==0:
      s[r1][c1] = v[r1][c1] + s[r1-1][c1]
    else:
      s[r1][c1] = v[r1][c1] + s[r1][c1-1] + s[r1-1][c1] - s[r1-1][c1-1]

answer = -11
for r1 in range(r):
  for r2 in range(r1, r):
    for c1 in range(c):
      for c2 in range(c1, c):
        if r1==0 and c1==0:
          sum = s[r2][c2]
        elif r1==0:
          sum = s[r2][c2] - s[r2][c1-1]
        elif c1==0:
          sum = s[r2][c2] - s[r1-1][c2]
        else:
          sum = s[r2][c2] - s[r2][c1-1] - s[r1-1][c2] + s[r1-1][c1-1]
        if sum > answer:
          answer = sum

print(answer)