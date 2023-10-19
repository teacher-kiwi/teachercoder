from collections import deque

# b0
# print(4)


# b1
buttons = "".join(input().split())
target = "00000000000000000000"
visited = set([buttons])
queue = deque([(buttons, 0)])
change = {
    "00": "11",
    "01": "10",
    "10": "01",
    "11": "00",
    "000": "111",
    "001": "110",
    "010": "101",
    "100": "011",
    "011": "100",
    "101": "010",
    "110": "001",
    "111": "000",
}

while queue:
    shape, step = queue.popleft()
    for i in range(20):
        if i == 0:
            temp = change[shape[:2]] + shape[2:]
        elif i == 19:
            temp = shape[:18] + change[shape[18:]]
        else:
            temp = shape[:i-1] + change[shape[i-1:i+2]] + shape[i+2:]

        if temp == target:
            print(step + 1)
            queue = None
            break
        if temp not in visited:
            queue.append((temp, step + 1))
            visited.add(temp)