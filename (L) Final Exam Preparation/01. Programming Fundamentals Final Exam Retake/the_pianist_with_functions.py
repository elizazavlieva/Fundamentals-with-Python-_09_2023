def add(piece_info, piece, composer, key):
    if piece in piece_info:
        print(f'{piece} is already in the collection!')
    else:
        piece_info[piece] = [composer, key]
        print(f'{piece} by {composer} in {key} added to the collection!')
    return piece_info


def remove(piece_info, piece):
    if piece in piece_info:
        piece_info.pop(piece)
        print(f'Successfully removed {piece}!')
    else:
        print(f'Invalid operation! {piece} does not exist in the collection.')
    return piece_info


def change_key(piece_info, piece, new_key):
    if piece in piece_info:
        piece_info[piece][1] = new_key
        print(f'Changed the key of {piece} to {new_key}!')
    else:
        print(f'Invalid operation! {piece} does not exist in the collection.')
    return piece_info


def solution(pieces_info):
    while True:
        command = input().split('|')
        if command[0] == 'Stop':
            break
        elif command[0] == 'Add':
            piece, composer, key = command[1], command[2], command[3]
            pieces_info = add(pieces_info, piece, composer,key)
        elif command[0] == 'Remove':
            piece = command[1]
            pieces_info = remove(pieces_info, piece)
        elif command[0] == 'ChangeKey':
            piece, new_key = command[1], command[2]
            pieces_info = change_key(pieces_info, piece, new_key)
    return pieces_info


def main(n):
    pieces_info = {}
    for pieces in range(n):
        info = input().split('|')
        piece, composer, key = info[0], info[1], info[2]
        pieces_info[piece] = [composer, key]
    pieces_info = solution(pieces_info)
    for key, value in pieces_info.items():
        print(f'{key} -> Composer: {value[0]}, Key: {value[1]}')


num_of_pieces = int(input())
main(num_of_pieces)
