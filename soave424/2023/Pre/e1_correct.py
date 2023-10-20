n = int(input())

# 남은 책상 수가 같으면 여러번 계산하지 말고 사용할 수 있도록 저장
cache = [[] for i in range(n+1)]

# 입력받은 책상 수 바탕으로 배열 만들기


def addDesks(leftDeskCount):
    result = [0] * (n + 1)
    result[leftDeskCount] = 1
    for i in range(2, leftDeskCount):
        if (len(cache[leftDeskCount - i]) == 0):
            cache[leftDeskCount - i] = addDesks(leftDeskCount - i)
        behindResult = cache[leftDeskCount - i]
        for j in range(2, len(behindResult)):
            result[i] += (i + j - 1) * behindResult[j]
    return result


answers = addDesks(n)

count = 0
for answer in answers:
    count += answer

print(count % 10000000)
