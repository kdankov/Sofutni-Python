needed_money = float(input())
owned_money = float(input())

days_count = 0
spending_days = 0

spending_five_days = False

while owned_money < needed_money and spending_days < 5:
    type_of_action = input()
    current_sum = float(input())
    days_count += 1
    
    if type_of_action == 'save':
        owned_money += current_sum
        spending_days = 0
    elif type_of_action == 'spend':
        if owned_money - current_sum < 0:
            owned_money = 0
        else:
            owned_money -= current_sum
        spending_days += 1
        
if spending_days == 5:
    print('You can\'t save the money.')
    print(f'{days_count}')
else:
    print(f'You saved the money for {days_count} days.')