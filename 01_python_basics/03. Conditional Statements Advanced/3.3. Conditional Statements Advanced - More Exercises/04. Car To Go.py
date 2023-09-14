budget = float(input())
season = input()

class_type = ''
car = ''
price = 0

if budget <= 100:
    class_type = 'Economy class'
    if season == 'Summer':
        car = 'Cabrio'
        price = budget * 0.35
    elif season == 'Winter':
        car = 'Jeep'
        price = budget * 0.65
elif budget <= 500:
    class_type = 'Compact class'
    if season == 'Summer':
        car = 'Cabrio'
        price = budget * 0.45
    elif season == 'Winter':
        car = 'Jeep'
        price = budget * 0.8
else:
    class_type = 'Luxury class'
    car = 'Jeep'
    price = budget * 0.9
    
print(class_type)
print(f'{car} - {price:.2f}')