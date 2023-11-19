import re

participants = input().split(', ')
pattern_of_names = r'[A-Za-z]'
pattern_of_distance = r'[0-9]'
results = {}
while True:
    command = input()
    if command == 'end of race':
        break
    name = ''.join(re.findall(pattern_of_names, command))
    distance = sum(int(num) for num in re.findall(pattern_of_distance, command))
    if name in participants:
        if name in results:
            results[name] += distance
        else:
            results[name] = distance

sorted_results = sorted(results.items(), key=lambda x: -x[1])
print(f'1st place: {sorted_results[0][0]}')
print(f'2nd place: {sorted_results[1][0]}')
print(f'3rd place: {sorted_results[2][0]}')
