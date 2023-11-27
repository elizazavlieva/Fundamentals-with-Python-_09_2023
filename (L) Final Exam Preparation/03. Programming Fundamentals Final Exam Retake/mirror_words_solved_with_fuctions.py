import re


def word_matches(text):
    pattern = r'(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'
    matches = re.findall(pattern, text)
    if len(matches):
        print(f'{len(matches)} word pairs found!')
    else:
        print('No word pairs found!')
    return matches


def solution(text):
    mirror_word = {}
    match = word_matches(text)
    for word in match:
        reversed_word = word[1][::-1]
        if reversed_word == word[2]:
            mirror_word[word[1]] = word[2]
    return mirror_word


line = input()
output = solution(line)
list_of_words =[]
if len(output):
    print('The mirror words are:')
    for k, v in output.items():
        list_of_words.append(f'{k} <=> {v}')
    print(', '. join(list_of_words))
else:
    print('No mirror words!')
