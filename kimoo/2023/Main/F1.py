# n = input()
# c = {"0":0, "1":0}
# for char in n:
#     c[char] += 1
# flag = True
# count = 0
# for char in n:
#     if flag and char == "1" or not flag and char == "0":
#         c[char] -= 1
#     else:
#         if flag and c["0"] > c["1"] or not flag and c["1"] > c["0"]:
#             # print("all")
#             count += 1
#             temp = c["0" if flag else "1"]
#             c["0"] = c["1" if flag else "0"]
#             c["1" if flag else "0"] = temp
#             flag = not flag
#         else:
#             # print("one")
#             count += 1
#             c[char] -= 1
# print(count)
    
n = int(input(), 2)
res = [float("inf")]

b = 1
while b < n:
    b *= 2
stack = [(0, b-1-n)]
while stack:
    i, n = stack.pop()
    if n == 0:
            res[0] = min(i, res[0])
    else:
        mask = 1 << (len(bin(n)) - 3)
        stack.append((i+1, n ^ mask))

        mask = 0
        for j in range(len(bin(n)) - 2):
            mask |= (1 << j)
        stack.append((i+1, n ^ mask))

print(res[0])