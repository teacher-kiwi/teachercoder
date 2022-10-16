
n,m=input().split(' ')
n=int(n)
m=int(m)


def factorial(x):
    n = 1
    for i in range(1,x+1):
        n = n*i 
    return n

c=factorial(int((n-1)+(m-1)))
a=factorial(n-1)
b=factorial(m-1)


print(int((c/(a*b))))
