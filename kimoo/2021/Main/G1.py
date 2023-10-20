from copy import deepcopy

# n, m = map(int, input().split())
# c = [list(map(int, input().split())) for _ in range(n)]
# x, y = map(int, input().split())

# test case1, answer = 3
# n, m = 5, 5
# c = [[0, 5, 7, 6, 4], [3, 1, 4, 3, 5], [7, 3, 7, 4, 5], [1, 2, 8, 3, 2], [7, 8, 6, 2, 5]]
# x, y = 4, 1

# test case2, answer = 0
# n, m = 5, 5
# c = [[0, 5, 7, 6, 4], [3, 1, 4, 3, 5], [7, 3, 7, 4, 5], [1, 2, 8, 3, 2], [7, 8, 6, 2, 5]]
# x, y = 1, 1

# test case3, answer = 4
n, m = 5, 5
c = [[0, 5, 7, 6, 4], [3, 1, 4, 3, 5], [7, 3, 7, 4, 5], [1, 2, 8, 3, 2], [7, 8, 6, 2, 5]]
x, y = 5, 4

# test case4, answer = 100
# n, m = 3, 3
# c = [[0, 100, 200],[1000, 100, 2],[100, 150, 22]]
# x, y = 2, 3 




# 길찾기 함수
def find_route():

  # 부스 비용을 오름차순으로 정리
  points = set()
  for li in c:
    points.update(li)
  points = sorted(list(points))

  print(points)
  return "test"
  # 타겟 설정
  goal = (x-1, y-1)

  # 타겟이 시작점이면 0 리턴
  if goal == (0,0):
    return 0

  # 가장 작은 비용부터 목표에 도달할 수 있는지 확인
  for point in points:

    # 위치설정(처음에는 좌상단에서 시작)
    positions = {(0,0)}
    
    while True:
      # 다음 칸 설정을 위해 임시 저장 공간 마련
      tmp = set()
      
      # 맵 복사
      cc = deepcopy(c)

      # 설정된 모든 위치에서 다음 칸 탐색
      for position in positions:

        # 상하좌우 네 방향 탐색
        for a in [(0,1), (1,0), (0,-1), (-1,0)]:
          next = (position[0]+a[0], position[1]+a[1])

          # 다음 칸 유효성 검사(벗어나는지, 왔던 길인지, 주어진 비용보다 큰지)
          if n <= next[0] or next[0] < 0 or m <= next[1] or next[1] < 0 or cc[next[0]][next[1]] == 0 or cc[next[0]][next[1]] > point:
            continue

          # 목표에 도착하면 반복 종료 후 현재 비용 리턴
          if next == goal:
            return point

          # 왔던 길 처리
          cc[next[0]][next[1]] = 0

          # 갈 수 있는 다음 칸 임시 저장
          tmp.add(next)
      
      # 모든 위치에서 갈 수 있는 다음 길이 없으면 다음 비용으로
      if len(tmp) == 0:
        break

      # 위치설정(저장된 다음 칸으로 변경)
      positions = tmp

print(find_route())