# 자릿값 합이 10인 수 중에서 11번째 수 찾기 
# TEST결과 : correct

list10=[]
for number in range(150):
  result=0
  for i in str(number):
    result += int(i)
    if result==10:
      list10.append(number)
print(list10[10])
