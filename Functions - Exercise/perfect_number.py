def perfect_num(number):
    num = 0
    for i in range(1, number):
        if number % i == 0:
            num += i
    if num == number:
        return 'We have a perfect number!'
    return 'It\'s not so perfect.'


user_input = int(input())
print(perfect_num(user_input))



