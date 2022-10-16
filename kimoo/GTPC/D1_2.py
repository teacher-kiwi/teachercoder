r, c = map(int, input().split())

v = []
for i in range(r):
  v.append(list(map(int, input().split())))

s = [[0 for _ in range(c+1)]]
for i in range(r):
  s.append([0])
  for j in range(c):
    if i == 0 and j == 0:
      s[i+1].append(v[i][j])
    elif i == 0:
      s[i+1].append(v[i][j] + s[i+1][j])
    elif j == 0:
      s[i+1].append(v[i][j] + s[i][j+1])
    else:
      s[i+1].append(v[i][j] + s[i+1][j] + s[i][j+1] - s[i][j])

sum = 0
for r1 in range(r):
  for r2 in range(r1, r):
    for c1 in range(c):
      for c2 in range(c1, c):
        new_sum = s[r1][c1] + s[r2+1][c2+1] - s[r1][c2+1] - s[r2+1][c1]
        sum = new_sum if new_sum > sum else sum

print(sum)
