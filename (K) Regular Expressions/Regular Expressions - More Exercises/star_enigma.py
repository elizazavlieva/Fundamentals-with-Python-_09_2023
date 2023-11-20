import re

n = int(input())
letters = ['s', 't', 'a', 'r']
attacked_planets = {"Attacked": [], "Destroyed": [], "A": "Attacked", "D": "Destroyed"}
pattern = re.compile(r"@(?P<planet_name>[A-Za-z]+)([^@\-!:>]*)"
                     r":(?P<population>[0-9]+)([^@\-!:>]*)"
                     r"(!)(?P<attack_type>[AD])\5([^@\-!:>]*)"
                     r"->(?P<soldier>[0-9]+)")

for line in range(n):
    current_message = input()
    decrypted_msg = sum(1 for letter in current_message if letter.lower() in letters)
    new_message = "".join(chr(ord(char) - decrypted_msg) for char in current_message)
    result = re.finditer(pattern, new_message)
    for show in result:
        attacked_planets[attacked_planets[show["attack_type"]]].append(show["planet_name"])

for type_attack in list(attacked_planets.keys())[:2]:
    planet_count = len(attacked_planets[type_attack])
    print(f"{type_attack} planets: {planet_count}")
    if planet_count:
        for planet in sorted(attacked_planets[type_attack]):
            print(f"-> {planet}")
