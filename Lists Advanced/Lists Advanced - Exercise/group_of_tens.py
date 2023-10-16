numbers = [int(num) for num in input().split(', ')]
group = 10
while True:
    if len(numbers) <= 0:
        break
    filtered_list = [num for num in numbers if num <= group]
    print(f'Group of {group}\'s: {filtered_list}')
    group += 10
    numbers = [ num for num in numbers if  num not in filtered_list]
