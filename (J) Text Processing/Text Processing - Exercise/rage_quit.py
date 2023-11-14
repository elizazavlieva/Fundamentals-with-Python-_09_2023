line = input()
message = ''
current_symbols = ''
repetition = ''
for i in range(len(line)):
    if not line[i].isdigit():
        current_symbols += line[i]
    else:
        for j in range(i, len(line)):
            if not line[j].isdigit():
                break
            repetition += line[j]
        message += current_symbols.upper() * int(repetition)
        current_symbols = ''
        repetition = ''

unique_symbols = set(message)
print(f'Unique symbols used: {len(unique_symbols)}\n{message}')
