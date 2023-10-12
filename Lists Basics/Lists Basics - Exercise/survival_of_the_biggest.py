numbers_str = input().split()

my_list = []

for num in numbers_str:
    my_list.append(int(num))

remover = int(input())

for i in range(remover):
    my_list.remove(min(my_list))

print(*my_list, sep=", ")