import re


def matches(places):
    pattern = r'(=|\/)([A-Z][A-Za-z]{2,})\1'
    return re.findall(pattern, places)


def solution(places):
    valid_matches = matches(places)
    points = sum([len(item[1]) for item in valid_matches])
    valid_places = [item[1] for item in valid_matches]
    print(f'Destinations: {", ".join(valid_places)}')
    print(f'Travel Points: {points}')


line = input()
solution(line)
