import re

text = input()
mirror_words = {}
pattern = r'(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'
matches = re.findall(pattern, text)
if len(matches) != 0:
    print(f'{len(matches)} word pairs found!')
else:
    print('No word pairs found!')

for line in matches:
    reversed_word = line[2][::-1]
    if line[1] == reversed_word:
        mirror_words[line[1]] = line[2]

if len(mirror_words) != 0:
    list_of_words = []
    print('The mirror words are:')
    for k, v in mirror_words.items():
        list_of_words.append(f'{k} <=> {v}')
    print(', '.join(list_of_words))
else:
    print('No mirror words!')
