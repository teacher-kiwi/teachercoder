n = int(input())
input()

sign = -1
answer = 0

for i in range(n, 1, -1):
  sign *= -1
  temp = 1
  if i != 2:
    for j in range(n, n-i+2, -1):
      temp *= j
      temp %= 1000000009

  answer += sign * temp
  
print(answer % 1000000009)