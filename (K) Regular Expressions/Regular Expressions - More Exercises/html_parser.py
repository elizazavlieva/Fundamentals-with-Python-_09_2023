import re

line = input()
title_pattern = r'<title>([^<>]*)<\/title>'

title = re.findall(title_pattern, line)
title = ''.join(title)
print(f"Title: {title}")

body_pattern = r'<body>.*<\/body>'
body = ''.join(re.findall(body_pattern, line))
pattern = r">([^><]*)<"
text = re.findall(pattern, body)
text = ''.join(text).replace('\\n', '')

print(f'Content: {text}')
