import math

n, m = map(int, input().split())

bread = n * m

if (bread <= 30):
    bread = 30
elif (bread <= 50):
    bread = 50
elif (bread <= 60):
    bread = 60
elif (bread <= 80):
    bread = 80
else:
    bread = math.ceil(bread / 10) * 10


print(bread * 300)