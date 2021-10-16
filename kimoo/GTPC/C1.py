n = int(input())

li = list(map(int, input().split()))



# 더 작은 거 돌아온다

# 가장 큰 거 두개 간다
# 가장 작은 거 한개 돌아온다

# 반복!

li2= []


res = 0
while(len(li) != 0):
    if(len(li) ==  2):
        res += max(li)
        break

    # 왼쪽 배가 한 척이면
    elif(len(li) ==  1):
        # 왼쪽 배 가고 끝
        li2.append(li[0])
        res += li[0]
        li.remove(li[0])
        break
    # 왼쪽 배가 2척 이상이면
    elif(len(li) > 1):
        # 가장 작은 거 두개 간다(->)
        min1 = min(li)
        li.remove(min1)
        li2.append(min1)
        min2 = min(li)
        li.remove(min2)
        li2.append(min2)

        res += min2

        # 가장 작은 게 온다(<-)
        min3 = min(li2)
        li2.remove(min3)
        li.append(min3)

        res += min3

        # 만약 왼쪽이 배가 1척이면
        if(len(li) == 1):
            # 그 배가 가고 끝
            li2.append[li[0]]
            res += li[0]
            li.remove[li[0]]
            break

        # 만약 왼쪽이 배가 2척 이상이면
        else:
            # 가장 큰 거 두개 보냄(->)
            max1 = max(li)
            li.remove(max1)
            max2 = max(li)
            li.remove(max2)

            li2.append(max1)
            li2.append(max2)

            res += max1
            if(len(li) == 0): break

            # 오른쪽에서 가장 작은거 한 개 옴
            min3 = min(li2)
            li2.remove(min3)
            li.append(min3)

            res += min3
            


print(res)