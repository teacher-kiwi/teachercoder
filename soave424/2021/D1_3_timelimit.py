# 자릿값 합이 k인 n번째 수 구하기 

k,n=input().split()
k=int(k)
n=int(n)
num=0

list_ksum=[]
while len(list_ksum)<n:
  num+=1
  result=0
  for i in str(num):
    result += int(i)
  if result==k:
    list_ksum.append(num)


print(list_ksum[-1])

