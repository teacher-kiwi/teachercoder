# # num = list(map(int, input().split()))
# n = int(input())
# original_list = list(map(int, input().split()))
# my_list = []


# def all_negative_or_zero(lst):
#     for num in lst:
#         if num > 0:
#             return False
#     return True


# while not all_negative_or_zero(original_list):
#     processed_numbers = ['.' if num <= 0 else 'O' for num in original_list]
#     result = '.'.join(processed_numbers)
#     my_list.append(result)
#     original_list = [x - 1 for x in original_list]

# for i in range(len(my_list) - 1, -1, -1):
#     print(my_list[i])

# 1초에는 대략 1억번, 글자 입출력은 백만자 정도 할 수 있음.
# 2차원 배열에 값을 저장하여 한번에 출력하거나 행 우선 탐색으로 2중 중첩반복문으로 직접 구성하며 바로 출력하는 방법이 있음.
# 아래는 두번째 방법인 행 우선 탐색, 행을 처리하느 반복문을 가장 큰 값부터 1까지 역순으로 반복하여 처리

# n = int(input())
# k = list(map(int, input(). split()))

n = 4
k = [2, 1, 4, 3]

cols = 2*n - 1
rows = max(k)


for h in range(rows, 0, - 1):
    for w in range(cols):
        if w % 2 == 0 and h <= k[w//2]:
            print("O", end="")
        else:
            print(".", end="")
    print()
