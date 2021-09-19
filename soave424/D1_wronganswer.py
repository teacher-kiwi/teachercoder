# 자릿값 합이 k인 n번째 수 구하기 
# TEST 결과 : Wrong
k,n=input().split()
k=int(k)
n=int(n)
if 10<=k<=19 and 1<=n<=10000:
  list_ksum=[]
  for number in range(70000):
    result=0
    for i in str(number):
      result += int(i)
      if result==k:
        list_ksum.append(number)
print(list_ksum[n-1])
