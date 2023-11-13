line = input()
letter = ''
result = ''

for i in line:
    if i != letter:
        result += i
        letter = i

print(result)
