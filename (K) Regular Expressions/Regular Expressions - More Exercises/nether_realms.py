import re
demon_name = re.split(r', *', input())

health_regex = r'[^\d\+\-*\/\.]'
damage_regex = r'(?:\+|-)?[0-9]+(?:\.[0-9]+)?'
operator_regex = r'[\*\/]'

demon_classification = {}
for demon in demon_name:
    demon = demon.strip()
    health = sum(ord(char) for char in re.findall(health_regex, demon))
    demon_classification[demon] = []
    demon_classification[demon].append(health)
    damage = re.finditer(damage_regex, demon)
    operation_symbols = re.findall(operator_regex, demon)
    current_dmg = 0
    for num in damage:
        current_dmg += float(num.group(0))
    for symbol in operation_symbols:
        if symbol == '*':
            current_dmg *= 2
        elif symbol == '/':
            current_dmg /= 2
    demon_classification[demon].append(current_dmg)

sorted_demons = dict(sorted(demon_classification.items()))
for participant, stats in sorted_demons.items():
    print(f'{participant} - {stats[0]} health, {stats[1]:.2f} damage')
