def solution(number, n):
    shifted_num = number >> n
    lsb = shifted_num & 1
    return lsb


user_input = int(input())
position = int(input())
print(solution(user_input, position))