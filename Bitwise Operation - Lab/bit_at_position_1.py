def solution(number):
    shifted_num = number >> 1
    lsb = shifted_num & 1
    return lsb


user_input = int(input())
print(solution(user_input))