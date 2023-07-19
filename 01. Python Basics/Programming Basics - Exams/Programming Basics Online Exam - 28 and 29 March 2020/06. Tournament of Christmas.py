days = int(input())

raised_money = 0
total_wins = 0
total_losses = 0

for i in range(days):
    current_money = 0
    current_wins = 0
    current_losses = 0
    
    sport = input()
    
    while sport != 'Finish':
        result = input()
        
        if result == 'win':
            current_money += 20
            current_wins += 1
        elif result == 'lose':
            current_losses += 1
        
        sport = input()
        
    if current_wins > current_losses:
        current_money *= 1.1
    
    raised_money += current_money
    total_wins += current_wins
    total_losses += current_losses

if total_wins > total_losses:
    raised_money *= 1.2
    print(f'You won the tournament! Total raised money: {raised_money:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {raised_money:.2f}')
