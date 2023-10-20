buttons = [True if c == "1" else False for c in input().split()]

step1, step2 = 0, 0
if True not in buttons:
    print(0)
else:
    copy_buttons = buttons[:]
    for i in range(19):
        if copy_buttons[i]:
            copy_buttons[i] = False
            copy_buttons[i+1] = not copy_buttons[i+1]
            if i != 18:
                copy_buttons[i+2] = not copy_buttons[i+2]
            step1 += 1

    buttons[0] = not buttons[0]
    buttons[1] = not buttons[1]
    step2 += 1
    for i in range(0, 19):
        if buttons[i]:
            buttons[i] = False
            buttons[i+1] = not buttons[i+1]
            if i != 18:
                buttons[i+2] = not buttons[i+2]
            step2 += 1
    print(min(step1, step2))