n = int(input())
count_positives = 0
sum_of_negatives = 0
positives = []
negatives = []
for i in range(n):
    num = int(input())
    if num < 0:
        sum_of_negatives += num
        negatives.append(num)
    else:
        count_positives += 1
        positives.append(num)
print(positives)
print(negatives)
print(f'Count of positives: {count_positives}')
print(f'Sum of negatives: {sum_of_negatives}')