# num = list(map(int, input().split()))
n = int(input())
original_list = list(map(int, input().split()))
my_list = []


def all_negative_or_zero(lst):
    for num in lst:
        if num > 0:
            return False
    return True


while not all_negative_or_zero(original_list):
    processed_numbers = ['.' if num <= 0 else 'O' for num in original_list]
    result = '.'.join(processed_numbers)
    my_list.append(result)
    original_list = [x - 1 for x in original_list]

for i in range(len(my_list) - 1, -1, -1):
    print(my_list[i])
