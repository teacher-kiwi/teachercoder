#투포환 던지기 결과
# 결과 correct

n=int(input())
pi=input()
t=float(input())

list=pi.split()

largest_so_far=100
champion=0
for i in list:
    i=float(i)
    the_num = abs(i-t)
    if the_num<largest_so_far :
        largest_so_far=the_num
        champion=i

print(f'{champion:.2f}')
