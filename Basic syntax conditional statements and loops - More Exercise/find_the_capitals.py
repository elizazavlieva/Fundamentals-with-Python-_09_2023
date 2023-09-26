word = input()
my_list = []

for i, index in enumerate(word):
    if index.isupper():
        my_list.append(i)
print(my_list)