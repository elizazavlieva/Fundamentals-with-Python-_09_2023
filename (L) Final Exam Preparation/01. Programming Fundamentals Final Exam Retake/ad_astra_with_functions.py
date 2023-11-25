import re


def matches(text):
    pattern = r'(\||#)([a-zA-Z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'
    return re.findall(pattern, text)


def solution(text):
    food_info = matches(text)
    days = sum(int(cal[3]) for cal in food_info) // 2000
    print(f'You have food to last you for: {days} days!')
    for items in food_info:
        print(f'Item: {items[1]}, Best before: {items[2]}, Nutrition: {items[3]}')


line = input()
solution(line)
