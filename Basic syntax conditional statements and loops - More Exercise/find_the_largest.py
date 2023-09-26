num = input()
my_list = []
new_num = 0
for i in num:
    my_list.append(int(i))

my_list.sort(reverse=True)
new_num = ''.join(map(str, my_list))
print(new_num)