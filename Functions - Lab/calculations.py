operator = input()
first_number = int(input())
second_number = int(input())


def calculations(a, b, operations):
    result = 0
    if operations == 'multiply':
        result = a * b
    elif operations == 'divide':
        result = int(a / b)
    elif operations == 'add':
        result = a + b
    elif operations == 'subtract':
        result = a - b
    return result


print(calculations(first_number, second_number, operator))
