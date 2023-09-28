snowballs = int(input())
result = 0
highest_weight = 0
highest_result = 0
best_time = 0
best_quality = 0

for i in range(1, snowballs + 1):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    result = (weight / time_needed) ** quality
    if result > highest_result:
        highest_result = result
        highest_weight = weight
        best_time = time_needed
        best_quality = quality
print(f'{highest_weight} : {best_time} '
      f'= {int(highest_result)} ({best_quality})')