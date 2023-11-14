start = ord(input())
end = ord(input())
line = input()
total = 0

for char in line:
    if start < ord(char) < end:
        total += ord(char)
print(total)
