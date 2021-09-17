list10=[]
for number in range(150):
  result=0
  for i in str(number):
    result += int(i)
    if result==10:
      list10.append(number)
print(list10[10])