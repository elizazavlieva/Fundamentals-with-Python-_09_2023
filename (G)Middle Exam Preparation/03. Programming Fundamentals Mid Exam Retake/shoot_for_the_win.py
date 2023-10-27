def solution(number):
    count = 0
    while True:
        command = input()
        if command == 'End':
            number = ' '.join(map(str, number))
            print(f'Shot targets: {count} -> {number}')
            break
        target = int(command)
        if target < len(number):
            for index, item in enumerate(number):
                if number[target] < item:
                    if target == index or item == -1:
                        continue
                    else:
                        number[index] -= number[target]
                else:
                    if target == index or item == -1:
                        continue
                    else:
                        number[index] += number[target]
            number[target] = -1
            count += 1
        else:
            continue

    return number


user_input = [int(num) for num in input().split()]
solution(user_input)

