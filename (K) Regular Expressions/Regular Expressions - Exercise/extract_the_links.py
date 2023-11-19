import re

while True:
    text = input()
    if len(text) == 0:
        break
    pattern = r'\b((www\.[a-zA-Z0-9\-]+)(\.[a-z]+)+)\b'
    matches = re.findall(pattern, text)
    if len(matches) != 0:
        for website in matches:
            print(''.join(website[0]))
