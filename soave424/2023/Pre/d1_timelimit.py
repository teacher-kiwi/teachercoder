a, b = map(int, input().split())


original_price = a  # 원래 상품의 가격
coupon_count = 0  # 사용한 쿠폰의 개수


while original_price > b:
    half_price = original_price // 2  # 원래 가격의 절반
    discounted_price = (half_price + 100) // 100 * 100  # 할인된 가격 (100원 미만 절삭)
    original_price = discounted_price  # 다음 루프를 위해 할인된 가격으로 업데이트
    coupon_count += 1  # 쿠폰 사용 횟수 증가

print(coupon_count)
