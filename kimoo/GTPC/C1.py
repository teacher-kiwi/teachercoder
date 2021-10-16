n = int(input())

li = list(map(int, input().split()))


# 가장 작은 거 두개 간다
# 더 작은 거 돌아온다

# 가장 큰 거 두개 간다
# 가장 작은 거 한개 돌아온다

# 반복!

li2= []


res = 0
while(len(li) != 0):
    if(len(li) > 1):
        min1 = min(li)
        li.remove(min1)
        min2 = min(li)
        li.remove(min2)

        li.append(min1)
        li2.append(min2)

        res += min1+min2

        if(len(li) == 1):
            res += li[0]
            break

        else:
            max1 = max(li)
            li.remove(max1)
            max2 = max(li)
            li.remove(max2)

            li2.append(max1)
            li2.append(max2)

            res += max1

            min3 = min(li2)
            li2.remove(min3)
            li.append(min3)

            res += min3
    else:
        li2.append(li[0])
        li.remove(li[0])
        res += li[0]
        



print(res)