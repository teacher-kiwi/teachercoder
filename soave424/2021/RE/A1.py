n,m = map(int, input().split())
nm=n*m
th_c_max = 0


if nm % 30 >0:
  th_c_max = (nm//30)+1
else:
  th_c_max = (nm//30)
  
coast = th_c_max*9000

for i in range(th_c_max):
  three = i
  if (nm-30*i)%50 > 0:
    five = (nm-30*i)//50 +1
  else:
    five = (nm-30*i)//50
  new_coast = three*9000 + five*15000
  if  coast > new_coast  :
    coast = new_coast
 
print(coast)