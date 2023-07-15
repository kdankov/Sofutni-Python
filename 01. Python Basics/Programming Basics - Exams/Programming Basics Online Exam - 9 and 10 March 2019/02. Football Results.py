first_match_result = input()
second_match_result = input()
third_match_result = input()

wins = 0
draws = 0
losses = 0

if first_match_result[0] > first_match_result[2]:
    wins += 1
elif first_match_result[0] < first_match_result[2]:
    losses += 1
else:
    draws += 1
    
if second_match_result[0] > second_match_result[2]:
    wins += 1
elif second_match_result[0] < second_match_result[2]:
    losses += 1
else:
    draws += 1
    
if third_match_result[0] > third_match_result[2]:
    wins += 1
elif third_match_result[0] < third_match_result[2]:
    losses += 1
else:
    draws += 1
    
print(f'Team won {wins} games.')
print(f'Team lost {losses} games.')
print(f'Drawn games: {draws}')