budget = float(input())
season = input()

location = ''
accommodation_place = ''
price = 0

if budget <= 1000:
    accommodation_place = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.65
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.45
elif budget <= 3000:
    accommodation_place = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.8
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.6
else:
    accommodation_place = 'Hotel'
    price = budget * 0.9
    if season == 'Summer':
        location = 'Alaska'
    elif season == 'Winter':
        location = 'Morocco'

print(f'{location} - {accommodation_place} - {price:.2f}')
