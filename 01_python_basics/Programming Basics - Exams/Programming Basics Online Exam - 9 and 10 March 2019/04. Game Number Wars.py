first_player_name = input()
second_player_name = input()

first_player_card = input()

first_player_points = 0
second_player_points = 0

has_winner = False

while first_player_card != 'End of game':
    second_player_card = input()
    
    first_player_card = int(first_player_card)
    second_player_card = int(second_player_card)
    
    if first_player_card > second_player_card:
        first_player_points += first_player_card - second_player_card
    elif first_player_card < second_player_card:
        second_player_points += second_player_card - first_player_card
    else:
        first_player_card = int(input())
        second_player_card = int(input())
        
        print('Number wars!')
        
        if first_player_card > second_player_card:
            print(f'{first_player_name} is winner with {first_player_points} points')
        else:
            print(f'{second_player_name} is winner with {second_player_points} points')
        
        has_winner = True
        break
    
    first_player_card = input()

if not has_winner:
    print(f'{first_player_name} has {first_player_points} points')
    print(f'{second_player_name} has {second_player_points} points')