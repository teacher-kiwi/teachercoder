a, b, c, d = map(int, input().split())


def check_zero(count, a, b, c, d):
    if (a, b, c, d) == (0, 0, 0, 0):
        print(count)
    else:
        check_zero(count+1, abs(a-b), abs(b-c), abs(c-d), abs(d-a))


check_zero(0, a, b, c, d)
