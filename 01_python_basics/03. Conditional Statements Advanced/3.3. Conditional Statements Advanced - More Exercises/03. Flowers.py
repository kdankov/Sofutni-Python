chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
isHoliday = input()

price = 0

if season == 'Spring' or season == 'Summer':
    price = chrysanthemums * 2 + roses * 4.10 + tulips * 2.50
elif season == 'Autumn' or season == 'Winter':
    price = chrysanthemums * 3.75 + roses * 4.50 + tulips * 4.15
    
if isHoliday == 'Y':
    price *= 1.15

if tulips > 7 and season == 'Spring':
    price *= 0.95

if roses >= 10 and season == 'Winter':
    price *= 0.9

if chrysanthemums + roses + tulips > 20:
    price *= 0.8
    
price += 2

print(f'{price:.2f}')