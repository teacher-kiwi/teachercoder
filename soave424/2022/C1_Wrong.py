n = int(input())
left = list(map(int, input().split()))
right = []
sum = 0


def check(right):
  right.sort()
  left.append(right[0])
  del right[0]


while len(left) > 0:  # 오른쪽으로 다 못 갔으면
  if len(left)==1:
    sum += left[0]
    break
  #왼쪽에서 가장 작은 값 2개 오른쪽으로 보내기
  left.sort()
  sum += left[1]
  right.extend(left[:2])
  del left[:2]
  # 여전히 왼쪽에 남아 있으면
  if len(left) > 0:
    # 오른쪽에서 가장 작은 값 1개 돌아오기
    sum += min(right)
    check(right)
    # 그런 다음 가장 큰 값 2개 오른쪽으로 보내기
    left.sort()
    sum += int(left[-1])
    right.extend(left[-2:])
    del left[-2:]
    if len(left) > 0:
      sum += min(right)
      check(right)

print(sum)