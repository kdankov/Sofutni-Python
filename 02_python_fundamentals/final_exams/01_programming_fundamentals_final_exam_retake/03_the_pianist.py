pieces_count = int(input())

pieces_dict = {}

for i in range(pieces_count):
    current_piece = input().split('|')
    piece = current_piece[0]
    composer = current_piece[1]
    key = current_piece[2]
    
    pieces_dict[piece] = [composer, key]
    
current_line = input()

while current_line != 'Stop':
    tokens = current_line.split('|')
    operation = tokens[0]
    
    if operation == 'Add':
        piece = tokens[1]
        composer = tokens[2]
        key = tokens[3]
        
        if piece not in pieces_dict:
            pieces_dict[piece] = [composer, key]
            print(f'{piece} by {composer} in {key} added to the collection!')
        else:
            print(f'{piece} is already in the collection!')
    
    elif operation == 'Remove':
        piece = tokens[1]
        
        if piece not in pieces_dict:
            print(f'Invalid operation! {piece} does not exist in the collection.')
        else:
            del pieces_dict[piece]
            print(f'Successfully removed {piece}!')
    
    elif operation == 'ChangeKey':
        piece = tokens[1]
        new_key = tokens[2]
        
        if piece not in pieces_dict:
            print(f'Invalid operation! {piece} does not exist in the collection.')
        else:
            pieces_dict[piece][1] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
        
    current_line = input()
    
for piece in pieces_dict:
    print(f"{piece} -> Composer: {pieces_dict[piece][0]}, Key: {pieces_dict[piece][1]}")
 
