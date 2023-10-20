
list = [
    ["income", 1, 1, 1000],
    ["outcome", 3, 15, 500],
    ["income", 2, 1, 1000],
    ["income", 6, 3, 1000],
    ["outcome", 11, 20, 3000],
    ["outcome", 12, 6, 2500],
    ["income", 4, 1, 2000],
    ["outcome", 1, 2, 150],
    ["income", 12, 5, 6500],
    ["outcome", 10, 9, 310]]


income_list = [0]*12
outcome_list = [0]*12

# line = int(input())

for i in list:
    # line = input()
    io = i[0]
    month = int(i[1])
    money = int(i[3])
    if io == "income":
        income_list[month-1] += money
    elif io == "outcome":
        outcome_list[month-1] += money


for i in range(12):
    month_print = i+1
    result = income_list[i] - outcome_list[i]
    print(i+1, income_list[i], outcome_list[i], result)
