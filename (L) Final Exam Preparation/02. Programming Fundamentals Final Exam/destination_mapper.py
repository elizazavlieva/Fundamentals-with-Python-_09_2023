import re

places = input()
destination = []
pattern = r'([=\/])([A-Z][a-zA-Z]{2,})(\1)'
matches = re.findall(pattern, places)
points = 0
for place in matches:
    points += len(place[1])
    destination.append(place[1])

print(f'Destinations: {", ".join(destination)}\nTravel Points: {points}')
