n = int(input())

for i in range(1, n + 1):
    sum_of_digit = 0
    digit = i
    while digit > 0:
        sum_of_digit += digit % 10
        digit = int(digit / 10)
    if (sum_of_digit == 5) or (sum_of_digit == 7) \
            or (sum_of_digit == 11):

        print(f'{i} -> True')
    else:
        print(f'{i} -> False')