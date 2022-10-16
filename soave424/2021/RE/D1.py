n, m = map(int, input().split())

num=0
num_result=0
digit_sum_cnt = 0

while digit_sum_cnt < m:
  num+=1
  digit = str(num)
  digit_sum = 0
  for i in digit:
    digit_sum += int(i)
    if digit_sum==n:
      digit_sum_cnt +=1
      num_result=num

print(num_result)