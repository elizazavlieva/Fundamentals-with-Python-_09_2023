text = [word for word in input().split() if len(word) % 2 == 0]

print(*text, sep='\n')
