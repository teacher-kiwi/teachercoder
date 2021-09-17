# 자릿값 합이 k인 n번째 수 구하기 
# TEST 결과 : Wrong
kn=input()
k=int(kn.split()[0])
n=int(kn.split()[1])
list_ksum=[]
for number in range(70000):
  result=0
  for i in str(number):
    result += int(i)
    if result==k:
      list_ksum.append(number)
print(list_ksum[n-1])
