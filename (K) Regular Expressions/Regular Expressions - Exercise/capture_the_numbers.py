import re
numbers = []
while True:
    text = input()
    if len(text) == 0:
        break
    pattern = '\\d+'
    matches = re.findall(pattern, text)
    if len(matches) != 0 :
        numbers.append(' '.join(matches))

print(' '.join(numbers))
