
def solution(list_items):
    repeated_items = {}
    for word in line:
        if word in repeated_items:
            repeated_items[word] += 1
        else:
            repeated_items[word] = 1
    return repeated_items


def odd_items(list_items):
    dictionary = solution(list_items)
    for k, v in dictionary.items():
        if v % 2 != 0:
            print(k, end=' ')


line = input().lower().split()

odd_items(line)
