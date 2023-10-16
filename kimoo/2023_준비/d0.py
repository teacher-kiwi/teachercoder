# d0
a, b = 150000, 5000

# d1
# a, b = map(int, input().split())

def solve(price: int, target: int):
    k = 0
    while True:
        if price <= target:
            print(k)
            return
        if price == 200:
            print(-1)
            return
        price = ((price // 2) + 100) // 100 * 100
        k += 1
        
solve(a, b)