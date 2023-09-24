divisor = int(input())
boundary = int(input())
my_list = []
for i in range(1, boundary + 1):
    if i % divisor == 0:
        my_list.append(i)
my_list.sort(reverse=True)

print(my_list[0])