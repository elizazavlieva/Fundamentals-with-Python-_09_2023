items = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
is_required = False
while True:
    line = input().lower().split()
    key = [line[i] for i in range(len(line)) if i % 2 != 0]
    value = [int(line[i]) for i in range(len(line)) if i % 2 == 0]
    for i in range(len(key)):
        if key[i] == 'shards' or key[i] == 'fragments' or key[i] == 'motes':
            items[key[i]] += value[i]
        else:
            if key[i] not in junk:
                junk[key[i]] = value[i]
            else:
                junk[key[i]] += value[i]
        for points in items.values():
            if points >= 250:
                is_required = True
                break
        if is_required:
            break
    if is_required:
        break

result = None
for k, v in items.items():
    if v >= 250:
        if k == 'shards':
            result = 'Shadowmourne'
        elif k == 'fragments':
            result = 'Valanyr'
        elif k == 'motes':
            result = 'Dragonwrath'
        items[k] -= 250
        if v < 0:
            v = 0
        print(f'{result} obtained!')

for k, v in items.items():
    print(f'{k}: {v}')
for k, v in junk.items():
    print(f'{k}: {v}')

