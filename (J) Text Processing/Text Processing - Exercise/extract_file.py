file_name = input()

start = 0
end = 0
for index in range(len(file_name)):
    if file_name[index] == '\\':
        start = index
    if file_name[index] == '.':
        end = index

print(f'File name: {file_name[start + 1:end]}\n'
      f'File extension: {file_name[end + 1:]}')
