import re

names = input()
patterns = '\\b[A-Z][a-z]+ [A-Z][a-z]+\\b'
matches = re.findall(patterns, names)
print(' '.join(matches))
