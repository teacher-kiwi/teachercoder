#투포환 던지기 결과
# 결과 correct

t=26.24
list=[15.76,5.96,17.14,14.26,12.78,3.42,12.50,12.43,14.24,29.40]	
largest_so_far=30
champion=0
for i in list:
    the_num = abs(i-t)
    if the_num<largest_so_far :
        largest_so_far=the_num
        champion=i

print(f'{champion:.2f}')
