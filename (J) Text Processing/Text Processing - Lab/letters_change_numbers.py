line = input().split()

letters = ''
number = 0
total = 0
for word in line:
    letters = word[0] + word[-1]
    number = int(word[1: -1])
    result = 0
    if letters[0].isupper():
        result = number / (ord(letters[0].lower()) - 96)
    elif letters[0].islower():
        result = number * (ord(letters[0]) - 96)
    if letters[1].isupper():
        result -= (ord(letters[1].lower()) - 96)
    elif letters[1].islower():
        result += (ord(letters[1]) - 96)
    total += result
print(f'{total:.2f}')
