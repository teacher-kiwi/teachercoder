

binary_string = input()  # 1과 0으로 이뤄진 문자열을 입력받음

count = 0  # 카운트를 저장할 변수
consecutive_zeros = False  # 연속된 0을 체크하는 플래그 변수

for digit in binary_string:
    if digit == '0':
        if not consecutive_zeros:
            count += 1
            consecutive_zeros = True
    else:
        consecutive_zeros = False

print(count)
