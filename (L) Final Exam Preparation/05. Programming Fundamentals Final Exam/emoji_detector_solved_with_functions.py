import re
from functools import reduce


def emoji_matches(text):
    pattern = r'(::|\*\*)([A-Z][a-z]{2,})(\1)'
    matches = re.findall(pattern, text)
    return matches


def threshold(text):
    pattern = r'\d'
    digits = [int(num) for num in re.findall(pattern, text)]
    return digits


some_string = input()
emoji = emoji_matches(some_string)
cool_threshold = reduce((lambda x, y: x * y), threshold(some_string))
print(f'Cool threshold: {cool_threshold}')
print(f'{len(emoji)} emojis found in the text. The cool ones are:')
for items in emoji:
    result = sum([ord(char) for char in items[1]])
    if result > cool_threshold:
        print(''.join(items))
