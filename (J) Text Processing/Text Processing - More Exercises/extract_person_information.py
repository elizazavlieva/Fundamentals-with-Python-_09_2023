n = int(input())
name = ''
age = ''
for i in range(n):
    line = input()
    if '@' in line and '|' in line:
        start = line.index('@') + 1
        end = line.index('|')
        name = line[start:end]
    if '#' in line and '*' in line:
        start = line.index('#') + 1
        end = line.index('*')
        age = line[start:end]
    print(f'{name} is {age} years old.')
