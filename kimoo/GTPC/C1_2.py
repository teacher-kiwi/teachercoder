n = int(input())
left = sorted(list(map(int, input().split())))
right = []
answer = 0

while len(left) > 3:
  answer += left[0] + min(left[1] * 2, left[0] + left[-2]) + left.pop()
  left.pop()

if len(left) < 3:
  answer += left[-1]
else:
  answer += sum(left)

print(answer)