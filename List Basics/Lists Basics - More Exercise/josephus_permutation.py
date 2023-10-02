initial_sequence = input(). split(' ')
executed_person = int(input())
order_of_execution = []
counter = 0
index = 0
while True:
    if len(initial_sequence) <= 0:
        break
    counter += 1
    if counter % executed_person == 0:
        order_of_execution.append(initial_sequence.pop(index))
    else:
        index += 1
    if index >= len(initial_sequence):
        index = 0
order_of_execution = list(map(int, order_of_execution))
print(repr(order_of_execution).replace(' ', ''))