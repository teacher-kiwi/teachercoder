import math 

# 최소공배수(LCM)를 구하는 함수
def lcm (a, b) :
  return a*b // math.gcd(a,b)

# 최대공약수(GCD)를 구하는 함수
def gcd(a,b) :
  if a % b == 0:
    return b
  else:
    return gcd(b, a%b)


# print(math.gcd(21,14)) # 최대공약수(GCD)
# print(gcd(21,14))
# print(lcm(21,14)) # 최소공배수(LCM)

n = int(input())
max = 0
for i in range(1,n+1):
  for j in range(n+1):
    lcm_ij = lcm(i,j)
    if lcm_ij > max :
      max = lcm_ij

print(max)