
def solution(food_list):
    key = [food_list[item] for item in range(len(food_list)) if item % 2 == 0]
    value = [int(food_list[item]) for item in range(len(food_list)) if item % 2 != 0]
    bakery = {key[i]: value[i] for i in range(len(key))}

    return bakery


user_input = input().split()
print(solution(user_input))

