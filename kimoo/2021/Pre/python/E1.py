data1 = input().split()
world = [int(data1[0]), int(data1[1])] #월드의 크기(행개수 r, 열개수 c)
target = [int(data1[2]), int(data1[3])] #목적지 좌표(tr, tc)

n = int(input()) #장애물의 개수
bList = []
for i in range(n):
    data2 = input().split()
    bList.append([int(data2[0]), int(data2[1])]) #장애물 리스트 저장(br, bc)

i = [[1, 1]] # 출발칸 및 움직인 후에는 자기 위치 저장
checkPoint = [] # 한 칸 움직였을 때 갈 수 있는 곳(체크포인트)을 저장
path = [] # 지나온 길을 저장(중복 방지 목적)
cnt = 0 # 몇 칸 움직였는지 카운트

if world == [1, 1]:
    print(0) # 예외처리: 월드크기가 1이면 0 출력
else:
    while target not in checkPoint and cnt != -1: # 목적지에 도착할 때까지 반복(예외처리: 길이 막히면 cnt에 -1 출력하고 반복 종료)
        checkPoint.clear() # 체크포인트 초기화
        for j in range(len(i)): # 자기 위치가 여러 개 일 경우 개수만큼 반복
            if [i[j][0]+1, i[j][1]] not in bList and [i[j][0]+1, i[j][1]] not in path and i[j][0]+1 <= world[0]:
                checkPoint.append([i[j][0]+1, i[j][1]]) # r방향으로 +1 움직였을 때, 장애물에 부딪히지 않고, 지나온 길이 아니고, 월드를 벗어나지 않으면 저장
            if [i[j][0]-1, i[j][1]] not in bList and [i[j][0]-1, i[j][1]] not in path and i[j][0]-1 > 0:
                checkPoint.append([i[j][0]-1, i[j][1]]) # r방향으로 -1 움직였을 때
            if [i[j][0], i[j][1]+1] not in bList and [i[j][0], i[j][1]+1] not in path and i[j][1]+1 <= world[1]:
                checkPoint.append([i[j][0], i[j][1]+1]) # c방향으로 +1 움직였을 때
            if [i[j][0], i[j][1]-1] not in bList and [i[j][0], i[j][1]-1] not in path and i[j][1]-1 > 0:
                checkPoint.append([i[j][0], i[j][1]-1]) # c방향으로 -1 움직였을 때
        for j in range(len(i)):
            path.append(i[j]) # 체크포인트를 지나온 길에 추가
        i.clear() # 내 위치 초기화
        if len(checkPoint) != 0:
            for j in range(len(checkPoint)): # 중복되는 체크포인트는 하나만 i에 저장
                if checkPoint[j] not in i:
                    i.append(checkPoint[j])
            cnt += 1
        else: # 체크포인트가 없으면(더이상 움직일 곳이 없으면) cnt에 -1(예외처리)
            cnt = -1

    print(cnt) # 목적지에 도착했을 때 움직인 칸수를 출력