product = input()
day = input()
quantity = float(input())

price = quantity

working_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
resting_days = ['Saturday', 'Sunday']

invalid = False

if day in working_days:
    if product == 'banana':
        price *= 2.50
    elif product == 'apple':
        price *= 1.20
    elif product == 'orange':
        price *= 0.85
    elif product == 'grapefruit':
        price *= 1.45
    elif product == 'kiwi':
        price *= 2.70
    elif product == 'pineapple':
        price *= 5.50
    elif product == 'grapes':
        price *= 3.85
    else:
        invalid = True
elif day in resting_days:
    if product == 'banana':
        price *= 2.70
    elif product == 'apple':
        price *= 1.25
    elif product == 'orange':
        price *= 0.90
    elif product == 'grapefruit':
        price *= 1.60
    elif product == 'kiwi':
        price *= 3.00
    elif product == 'pineapple':
        price *= 5.60
    elif product == 'grapes':
        price *= 4.20
    else:
        invalid = True
else:
    invalid = True
    
if invalid:
    print('error')
else:
    print(f'{price:.2f}')