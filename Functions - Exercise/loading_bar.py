def loading_bar(number):
    num = number // 10
    ready = '%' * num
    remind = '.' * (10 - num)
    loading = ready + remind
    return loading


user_input = int(input())
if user_input == 100:
    print('100% Complete!')
    print(f'[{loading_bar(user_input)}]')
else:
    print(f'{user_input}% [{loading_bar(user_input)}]')
    print('Still loading...')
