head = input()
body = input()
tail = input()


my_list = [head, body, tail]
my_list[0], my_list[2] = my_list[2], my_list[0]

print(my_list)