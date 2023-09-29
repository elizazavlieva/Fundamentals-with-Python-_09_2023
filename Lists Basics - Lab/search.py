n = int(input())
word = input()
my_list = []
for i in range(n):
    input_string = input()
    my_list.append(input_string)
print(my_list)

matches = []

for match in my_list:
    if word in match:
        matches.append(match)
print(matches)