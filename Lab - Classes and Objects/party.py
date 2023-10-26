class Party:
    people = []

    def __init__(self):
        pass


counter = 0
while True:
    name = input()
    if name == 'End':
        break
    Party.people.append(name)
    counter += 1

print(f'Going: {", ".join(Party.people)}')
print(f'Total: {counter}')
