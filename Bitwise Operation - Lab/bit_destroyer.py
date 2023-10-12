def solution(number, n):
    mask = 1 << n
    reversed_mask = ~ mask
    new_num = number & reversed_mask
    return new_num


user_input = int(input())
position = int(input())

print(solution(user_input, position))

