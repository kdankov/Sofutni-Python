budget = float(input())
destination = input()
season = input()
days = int(input())

total_sum = 0

if destination == 'Dubai':
    if season == 'Winter':
        total_sum = 45000 * days
    elif season == 'Summer':
        total_sum = 40000 * days
    
    total_sum *= 0.7
elif destination == 'Sofia':
    if season == 'Winter':
        total_sum = 17000 * days
    elif season == 'Summer':
        total_sum = 12500 * days
    
    total_sum *= 1.25
elif destination == 'London':
    if season == 'Winter':
        total_sum = 24000 * days
    elif season == 'Summer':
        total_sum = 20250 * days
    
if total_sum <= budget:
    print(f'The budget for the movie is enough! We have {budget - total_sum:.2f} leva left!')
else:
    print(f'The director needs {total_sum - budget:.2f} leva more!')