line = input()
result = ''
power = 0
for i in range(len(line)):
    if line[i] == '>':
        result += line[i]
        power += int(line[i + 1])
    elif power > 0 and line[i] != '>':
        power -= 1

    else:
        result += line[i]
print(result)
