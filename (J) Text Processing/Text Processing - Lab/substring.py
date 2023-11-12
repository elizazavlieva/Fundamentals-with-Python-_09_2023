command = input()
line = input()

while True:
    if command in line:
        line = line.replace(command, '')
    else:
        break
print(line)
