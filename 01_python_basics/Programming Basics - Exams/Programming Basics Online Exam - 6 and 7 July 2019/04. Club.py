target_sum = float(input())

collected_sum = 0

cocktail_name = input()

is_enough = False

while(cocktail_name != 'Party!'):
    cocktails_count = int(input())
    current_sum = 0
    
    current_sum = len(cocktail_name) * cocktails_count
    
    if current_sum % 2 != 0:
        current_sum *= 0.75
    
    collected_sum += current_sum
    
    if collected_sum >= target_sum:
        is_enough = True
        break
    
    cocktail_name = input()
    
if is_enough:
    print('Target acquired.')
else:
    print(f'We need {target_sum - collected_sum:.2f} leva more.')

print(f'Club income - {collected_sum:.2f} leva.')