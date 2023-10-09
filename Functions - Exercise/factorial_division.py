import math


def factorial_division (first, second):
    first_factorial = math.factorial(first)
    second_factorial = math.factorial(second)
    division = first_factorial / second_factorial
    return f'{division:.2f}'


first_num = int(input())
second_num = int(input())
print(factorial_division(first_num, second_num))
