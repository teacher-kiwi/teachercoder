# f0
n = 3
nums = [4, 1, 5]


# f1
# n = int(input())
# nums = list(map(int, input().split()))

max_num = max(nums)

while max_num:
    temp = ""
    for num in nums:
        if num < max_num:
            temp += "."
        else:
            temp += "O"
        temp += "."
    print(temp[:-1])
    max_num -= 1