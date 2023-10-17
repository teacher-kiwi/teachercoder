# N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수

n, k = map(int, input().split())
number = list(input())

answer = []
cnt = k
for num in number:
    while answer and cnt > 0 and answer[-1] < num:
        del answer[-1]
        cnt -= 1
    answer.append(num)

print(''.join(answer[:n-k]))

# 맨 왼쪽에 가장 큰 수가 오도록 지우는 것이 좋음.
# 스택을 사용하면 시간복잡도 가능하게 됨.
# 스택의 개념, 필요성, 구현 역량 필요
# 스택은 입력이 들어온 순서대로 밑에서부터 차곡차곡 쌓아가고 나중에 입력된 데이터를 가장 먼저 출력함.
