R, C = map(int, input(). split())
a=[list(map(int,input().split())) for _ in range(R)]


def pS2(a):
  global C, R
  psa = [[0 for x in range(C)] for y in range(R)]
  psa[0][0] = a[0][0]
  for i in range(1,C) : 
    psa[0][i]= psa[0][i-1]+a[0][i]
  for i in range(0, R) :
    psa[i][0] = psa[i-1][0]+a[i][0]
  for i in range(1,R) :
    for j in range(1, C) :
      psa[i][j] = psa[i-1][j]+psa[i][j-1]-psa[i-1][j-1]+a[i][j]
  return(psa)

def pSum(prsum):
  global a, C, R
  ans=-11
  for i in range(R):
    for j in range(C):
      for ii in range(i, R):
        for jj in range(j, C):
          t=prsum[ii][jj]
          if j-1<0 :
            b=0
            d=0
          else:
            b=prsum[ii][j-1]
            d=prsum[i-1][j-1]
          if i-1<0:
            c=0
            d=0
          else:
            c=prsum[i-1][jj]
          ans=max(ans, t-b-c+d)
  return(ans)

prsum=pS2(a)
print(pSum(prsum))