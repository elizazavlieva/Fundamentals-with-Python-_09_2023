capacity = 255
n = int(input())
total = 0
for i in range(n):
    litres = int(input())
    if capacity >= litres:
        capacity -= litres
        total += litres
    else:
        print('Insufficient capacity!')

print(total)