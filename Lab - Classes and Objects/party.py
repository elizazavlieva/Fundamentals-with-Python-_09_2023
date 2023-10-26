class Party:
    def __init__(self):
        self.people = []


party = Party()
counter = 0
while True:
    name = input()
    if name == 'End':
        break
    party.people.append(name)
    counter += 1

print(f'Going: {", ".join(party.people)}')
print(f'Total: {counter}')
