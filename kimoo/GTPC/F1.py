from re import A
from string import ascii_uppercase
abc = list(ascii_uppercase) + [l1+l2 for l1 in ascii_uppercase for l2 in ascii_uppercase] + [l1+l2+l3 for l1 in ascii_uppercase for l2 in ascii_uppercase for l3 in ascii_uppercase]

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a2 = sorted(enumerate(a), key=lambda x: x[1], reverse=True)
b2 = sorted(enumerate(b), key=lambda x: x[1], reverse=True)
c2 = list(map(lambda x: x[1][0] ,sorted(list(map(lambda x, y: [x, y], a2, b2)), key=lambda x: x[0][0])))

answer1 = sum(list(map(lambda x, y: x[1] * y[1],a2, b2)))
answer2 = " ".join(list(map(lambda x: abc[x], c2)))

print(answer1)
print(answer2)