from math import trunc


def solution(number, binary_digit):
    counter = 0
    while number > 0:
        remainder = number % 2
        number = trunc(number / 2)
        if remainder == binary_digit:
            counter += 1
    return counter


num = int(input())
digit = int(input())
print(solution(num, digit))