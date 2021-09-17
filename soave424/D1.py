kn=input()
k=int(kn.split()[0])
n=int(kn.split()[1])
list_ksum=[]
for number in range(999):
  result=0
  for i in str(number):
    result += int(i)
    if result==k:
      list_ksum.append(number)
print(list_ksum[n-1])
