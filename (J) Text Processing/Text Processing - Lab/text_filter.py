words = input().split(', ')
text = input()

for word in words:
    while True:
        if word in text:
            text = text.replace(word, '*' * len(word))
        else:
            break
print(text)
