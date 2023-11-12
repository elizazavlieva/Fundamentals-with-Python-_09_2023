command = input().split(' ')
result = ''
for word in command:
    length = len(word)
    result += word * length
print(result)
