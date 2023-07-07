width = int(input())
length = int(input())

pieces = width * length

while pieces > 0:
    current_pieces = input()
    
    if str(current_pieces) == 'STOP':
        break
    
    pieces -= int(current_pieces)
    
    
if pieces >= 0:
    print(f'{pieces} pieces are left.')
else:
    print(f'No more cake left! You need {abs(pieces)} pieces more.')