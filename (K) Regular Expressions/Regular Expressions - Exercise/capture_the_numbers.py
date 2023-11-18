import re

while True:
    text = input()
    if len(text) == 0:
        break
    pattern = '\\d+'
    matches = re.findall(pattern, text)
    if len(matches) != 0:
        print(' '.join(matches), end=' ')

