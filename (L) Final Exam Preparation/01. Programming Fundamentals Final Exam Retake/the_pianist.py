n = int(input())
collection = {}
for line in range(n):
    piece_info = input().split('|')
    collection[piece_info[0]] = [piece_info[1], piece_info[2]]
while True:
    command = input().split('|')
    if command[0] == 'Stop':
        break
    if command[0] == 'Add':
        piece, composer, key = command[1], command[2], command[3]
        if piece in collection:
            print(f'{piece} is already in the collection!')
        else:
            collection[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif command[0] == 'Remove':
        piece = command[1]
        if piece in collection:
            collection.pop(piece)
            print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')
    elif command[0] == 'ChangeKey':
        piece, key = command[1], command[2]
        if piece in collection:
            collection[piece][1] = key
            print(f'Changed the key of {piece} to {key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

for k, v in collection.items():
    print(f'{k} -> Composer: {v[0]}, Key: {v[1]}')
