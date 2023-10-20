buttons = "".join(input().split())
# buttons = "01110011100111000111"
# buttons = "00111001101100000000"
# buttons = "00000000000000000000"
# buttons = "11111000000000000111"
# buttons = "00100000000000000000"

target = "00000000000000000000"
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
res = set()

def solve(i, buttons, count):
    if buttons == target:
        res.add(count)
        return
    if i > 19:
        return
    
    solve(i+1, buttons, count)
    if i == 0:
        temp = change[buttons[:2]] + buttons[2:]
    elif i == 19:
        temp = buttons[:18] + change[buttons[18:]]
    else:
        temp = buttons[:i-1] + change[buttons[i-1:i+2]] + buttons[i+2:]
    solve(i+1, temp, count+1)

solve(0, buttons, 0)
print(min(res))
