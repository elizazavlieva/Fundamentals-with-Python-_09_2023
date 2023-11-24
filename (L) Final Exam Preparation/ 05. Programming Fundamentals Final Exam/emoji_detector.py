import re
from functools import reduce
text = input()

emoji_pattern = r'(::|\*\*)([A-Z][a-z]{2,})(\1)'
threshold_pattern = r'\d'

emojis = [list(tup) for tup in re.findall(emoji_pattern, text)]
threshold = [int(num) for num in ''.join(re.findall(threshold_pattern, text))]
cool_threshold = reduce((lambda x, y: x * y), threshold)

print(f'Cool threshold: {cool_threshold}\n{len(emojis)} emojis found in the text. The cool ones are:')

for index in range(len(emojis)):
    emoji_coolness = sum([ord(char) for char in emojis[index][1]])
    if emoji_coolness > cool_threshold:
        print(f'{"".join(emojis[index])}')
