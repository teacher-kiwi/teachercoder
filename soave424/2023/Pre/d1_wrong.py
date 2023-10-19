def binary_search(a, b):
    left, right = 1, a  # 이진 탐색의 시작 범위를 설정합니다.
    answer = a  # 최종적으로 반환할 답을 저장할 변수를 초기화합니다.

    # 이진 탐색을 수행합니다.
    while left <= right:
        mid = (left + right) // 2  # 중간 값 계산
        half_price = a // (2 ** mid)  # 현재 중간 값에 해당하는 할인된 가격 계산
        discounted_price = (half_price + 100) // 100 * \
            100  # 할인된 가격 (100원 미만 절삭)

        # 할인된 가격이 b 이하인 경우, 더 작은 쿠폰 개수로 시도해 봅니다.
        if discounted_price <= b:
            answer = mid  # 현재 시도한 쿠폰 개수를 정답으로 저장
            right = mid - 1  # 더 작은 쿠폰 개수를 시도하기 위해 범위를 왼쪽으로 좁힘
        else:
            left = mid + 1  # 할인된 가격이 b보다 큰 경우, 더 큰 쿠폰 개수로 시도해 봅니다.

    return answer


# 입력 받기
a, b = map(int, input().split())

# 결과 출력
print(binary_search(a, b))
