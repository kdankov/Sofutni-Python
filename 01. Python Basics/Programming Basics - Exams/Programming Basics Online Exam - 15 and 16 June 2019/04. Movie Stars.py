budget = float(input())

command = input()

is_not_enough = False

while command != 'ACTION':
    actor = command
    if len(actor) <= 15:
        budget -= float(input())
    else:
        budget -= budget * 0.2

    if budget < 0:
        is_not_enough = True
        break
    
    command = input()
    
if is_not_enough:
    print(f'We need {abs(budget):.2f} leva for our actors.')
else:
    print(f'We are left with {budget:.2f} leva.')