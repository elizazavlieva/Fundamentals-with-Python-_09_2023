first_line, second_line = input().split()
result = 0
if len(first_line) > len(second_line):
    for i in range(len(second_line)):
        result += ord(first_line[i]) * ord(second_line[i])
    for j in range(len(second_line), len(first_line)):
        result += ord(first_line[j])
elif len(first_line) < len(second_line):
    for i in range(len(first_line)):
        result += ord(first_line[i]) * ord(second_line[i])
    for j in range(len(first_line), len(second_line)):
        result += ord(second_line[j])
else:
    for i in range(len(first_line)):
        result += ord(first_line[i]) * ord(second_line[i])
print(result)
